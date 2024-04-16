import streamlit as st
import re
from test_case import test_case


st.set_page_config(layout="wide")


def remove_header(mail):
    pattern = re.compile(r"^.*?(?=Subject:)", re.DOTALL)
    mail = re.sub(pattern, "", mail)
    pattern = re.compile(r"^To:.*$", re.MULTILINE)
    mail = re.sub(pattern, "", mail)
    return mail


def process_one_mail(mail):
    """
    remove signature, but keep the first line of the signature,
    usually the name of the sender
    """

    body = remove_header(mail)
    sig_separtor = [
        r"^[>| ]*Thanks,$",
        r"^[>| ]*Thank you,$",
        r"^[>| ]*Best regards[,]?$",
        r"^[>| ]*Cordialement[,]?$",
        r"^[>| ]*[-|_|\*|=]{2,}[ ]*$",
    ]
    sig_separtor_regex = re.compile(
        "|".join(sig_separtor), re.MULTILINE | re.IGNORECASE
    )
    try:
        body, signature = re.split(sig_separtor_regex, body, maxsplit=1)
    except Exception:
        # No signature found, do nothing
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
    - If the email contains all the keywords: "Sent:", "From:", "To:", "Subject:",
    and all at the beginning of the line
    """
    return all(
        re.search(f"^{keyword}", text, re.MULTILINE)
        for keyword in ["Sent:", "From:", "To:", "Subject:"]
    )


def process(text):
    """
    main function to process the email
    """
    if not need_to_process(text):
        st.info("No need to process")
        return text

    forward_pattern = [
        r"-+Original Message-+",
        r"-+ Forwarded message -+",
        r"-+ Message transféré -+",
        r"-+Message d'origine-+",
        r"On [\w| |,]*:\d{2}[a-zA-Z ]*,[a-zA-Z <>@\.]*wrote[\n ]?:",
        r"Le \d{1,2} [A-Za-z]+ \d{4} \d{1,2}:\d{2}, .* <.*> a écrit[\n ]?:",
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
