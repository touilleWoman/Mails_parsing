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


def clean_signature(body):
    # Detect signature block
    pattern = re.compile(r"(--\s*\n)([\s\S]*)", re.DOTALL)
    match = pattern.search(body)
    if match:
        _separator = match.group(1)
        signature = match.group(2)
        # Define patterns to remove phone numbers, emails, and web links
        phone_pattern = re.compile(
            r"\b(?:tel|phone|fax):\s*[\d\s()+-]+\b", re.IGNORECASE
        )
        email_pattern = re.compile(r"\b[\w.-]+@[\w.-]+\.\w+\b")
        link_pattern = re.compile(r"\b(?:www\.)?[\w-]+\.\w{2,}\b")

        # Remove identified items
        signature = phone_pattern.sub("", signature)
        signature = email_pattern.sub("", signature)
        signature = link_pattern.sub("", signature)

        # Replace the original signature with the cleaned version
        body = body[: match.start()] + signature

    return body


def process_one_mail(mail):
    """
    remove signature, but keep the first line of the signature,
    usually the name of the sender
    """

    body = remove_header(mail)
    body = clean_signature(body)
    return body


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
    on = st.toggle('Show Code')
    if on:
        regex_code = """
def remove_header(mail):
    pattern = re.compile(r"^.*?(?=Subject:)", re.DOTALL)
    mail = re.sub(pattern, "", mail)
    pattern = re.compile(r"^To:.*$", re.MULTILINE)
    mail = re.sub(pattern, "", mail)
    return mail


def clean_signature(body):
    # Detect signature block
    pattern = re.compile(r"(--\s*\n)([\s\S]*)", re.DOTALL)
    match = pattern.search(body)
    if match:
        _separator = match.group(1)
        signature = match.group(2)
        # Define patterns to remove phone numbers, emails, and web links
        phone_pattern = re.compile(
            r"\b(?:tel|phone|fax):\s*[\d\s()+-]+\b", re.IGNORECASE
        )
        email_pattern = re.compile(r"\b[\w.-]+@[\w.-]+\.\w+\b")
        link_pattern = re.compile(r"\b(?:www\.)?[\w-]+\.\w{2,}\b")

        # Remove identified items
        signature = phone_pattern.sub("", signature)
        signature = email_pattern.sub("", signature)
        signature = link_pattern.sub("", signature)

        # Replace the original signature with the cleaned version
        body = body[: match.start()] + signature

    return body


def process_one_mail(mail):
    \"\"\"
    remove signature, but keep the first line of the signature,
    usually the name of the sender
    \"\"\"

    body = remove_header(mail)
    body = clean_signature(body)
    return body


def need_to_process(text):
    \"\"\"
    Check if the email needs to be processed:
    - If the email contains all the keywords: "Sent:", "From:", "To:", "Subject:",
    and all at the beginning of the line
    \"\"\"
    return all(
        re.search(f"^{keyword}", text, re.MULTILINE)
        for keyword in ["Sent:", "From:", "To:", "Subject:"]
    )


def process(text):
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
    """
    
        st.code(regex_code, language="python")

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
