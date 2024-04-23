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
        r"^De :.*@.*$",  # French headers below
        r"^À :.*$",
        r"^Bcc : .*$",
        r"^Date[ ]?: .*$",
    ]
    pattern = re.compile("|".join(headers_pattern), re.MULTILINE)
    mail = re.sub(pattern, "", mail)
    return mail


def process_one_mail(body):
    """
    remove signature, try to grab the writer's name from the signature and keep it.
    """

    # List of regex patterns for different signature separators
    sig_separators = [
        r"^[>| ]*Thanks[,!]$",
        r"^[>| ]*Thank you,$",
        r"^[>| ]*All my best,$",
        r"^[>| ]*Best regards[,]?$",
        r"^[>| ]*Cordialement[,]?$",
        r"^[>| ]*[-|_|\*|=]{2,}[ ]*$",
        r"\[image: Petzl\]",
    ]

    # List of end patterns (URLs in this case)
    end_patterns = [
        r"www\.petzldealer\.com",
        r"www\.petzlsolutions\.com" r"www\.petzl\.com",
        r"http:\/\/www\.wpic\.co\/",
    ]
    start_pattern = "|".join(sig_separators)
    end_pattern = "|".join(end_patterns)

    # a non-greedy search
    regex_pattern = re.compile(
        f"({start_pattern})([\\s\\S]*?)({end_pattern})", re.MULTILINE | re.IGNORECASE
    )

    match = re.search(regex_pattern, body)
    if not match:
        return body
    else:
        # try to grab the writer's name from the signature
        signature = match.group(2)
        first_name = ""
        last_name = ""
        for line in signature.split("\n"):
            match_name = re.search(
                r"^\*?([A-Z][a-z]+)([\s•\*]{0,3}([A-Z][a-z]+))?\*?$", line
            )
            if match_name and len(line) < 20:
                first_name = match_name.group(1)
                if len(match_name.groups()) == 3:
                    last_name = " " + match_name.group(3)
                break
        return (
            body[: match.start()] + first_name + last_name + "\n" + body[match.end() :]
        )


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
    main function to process the emails
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
        r"On .*, .* <.*>[\n ]?wrote[\n ]?:",
        r"Le .*, .* <.*>[\n ]?a écrit[\n ]?:",
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
