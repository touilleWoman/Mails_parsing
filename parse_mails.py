import streamlit as st
import re
from test_case import test_case


st.set_page_config(layout="wide")


def remove_header(mail):
    headers_pattern = [
        r"^Sent:.*$",
        r"^From:.*@.*$",
        r"^To:.*$",
        r"^Cc:.*$",
        r"^Bcc:.*$",
        r"^De :.*@.*$", # French headers below
        r"^À :.*$",
        r"^Bcc : .*$",
        r"^Date[ ]?: .*$",
    ]
    pattern = re.compile("|".join(headers_pattern), re.MULTILINE)
    mail = re.sub(pattern, "", mail)
    return mail

def match_petzel(text):
    """
    match the bloc of signature: 
    - with tel or fax followed by www.petzl.com, but no more than 1 empty line between them
    - with www.petzl.com, without empty line
    """
    
    pattern = [
        r"(?:(?!\n\n).)*\b(tel|fax)\b(?:(?!\n\n\n).)*www\.petzl\.com",
        r"(?:(?!\n\n).)*(www\.petzl\.com|\bPetzl America\b)",
    ]
    match = re.search('|'.join(pattern), text, re.IGNORECASE | re.DOTALL)
    if match :
        body = text[:match.start()]
        signature = text[match.start():]
    return body, signature



def process_one_mail(body):
    """
    remove signature, but keep the first line of the signature,
    usually the name of the sender
    """

    sig_separtor = [
        r"^[>| ]*Thanks,$",
        r"^[>| ]*Thank you,$",
        r"^[>| ]*Best regards[,]?$",
        r"^[>| ]*Cordialement[,]?$",
        r"^[>| ]*[-|_|\*|=]{2,}[ ]*$",
    ]
    # search [image: Petzl] as a string
    sig_separtor.append(re.escape("[image: Petzl]"))
    
    sig_separtor_regex = re.compile(
        "|".join(sig_separtor), re.MULTILINE | re.IGNORECASE
    )
    signature = None
    try:
        # if mail contains sig_pattern, split the mail into body and signature
        body, signature = re.split(sig_separtor_regex, body, maxsplit=1)
    except Exception:
        # no sig_pattern, try to identify signature with petzel pattern
        body, signature = match_petzel(body)
    finally:
        if not signature:
            return body
        else:
            # try to grab the writer's name from the signature
            name = ""
            for line in signature.split("\n"):
                if re.search(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\b", line) and len(line) < 20:
                    name = line
                    break
            return body + name


def need_to_process(text):
    """
    Check if the email needs to be processed:
    - If the email contains any of the keywords: "Sent:", "From:", "To:", "Subject:",
    at the beginning of the line
    """
    return any(
        re.search(f"^{keyword}", text, re.MULTILINE)
        for keyword in ["Sent:", "From:", "To:", "Subject:", "De :", "À :"]
    )


def process(text):
    """
    main function to process the email
    """
    if not need_to_process(text):
        st.info("No need to process")
        return text
    text = remove_header(text)
    forward_pattern = [
        r"-+Original Message-+",
        r"-+ Forwarded message -+",
        r"-+ Message transféré -+",
        r"-+Message d'origine-+",
        r"On [\w| |,]*:\d{2}[a-zA-Z ]*,[a-zA-Z <>@\.]*wrote[\n ]?:",
        r"Le .*, .* <.*> a écrit[\n ]?:",
    ]
    forward_regex = re.compile("|".join(forward_pattern), re.IGNORECASE | re.MULTILINE)

    separated = re.split(forward_regex, text)
    cleaned = ""
    for mail in separated:
        if mail:
            cleaned += process_one_mail(mail)
    return cleaned


def process_and_display(text):
    processed_text = process(text)

    col1, col2 = st.columns(2)

    with col1:
        st.title("Before:")
        st.markdown(f"""```\n{text}\n```""")

    with col2:
        st.title("After:")
        st.markdown(f"""```\n{processed_text}\n```""")


def main():
    st.title("Process Emails with Regex")

    # Text area for user input
    user_input = st.text_area(
        "Paste an email Here, then Press Ctrl + Enter to apply ", height=300
    )

    if user_input:
        # Process the text with your regex function

        process_and_display(user_input)

    st.divider()

    st.title("A few Test Cases")

    for text in test_case():
        process_and_display(text)
        st.divider()


if __name__ == "__main__":
    main()
