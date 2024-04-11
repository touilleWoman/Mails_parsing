import streamlit as st
import re
from test_case import test_case


st.set_page_config(layout="wide")


def remove_signature(body):
    """
    remove signature, but keep the first line of the signature,
    usually the name of the sender
    """

    signature_patterns = [
        r"^\s*--\s*$",  # Common signature separator
        r"^Regards(,|\s)",  # Common closing
        r"^Best(,|\s)",
        r"^Sincerely(,|\s)",
        r"^(Tel|Fax)(:|\s)",
        r"Site Crolles - Cidex",  # Another example specific line
    ]

    # Combine the patterns into a single regex
    signature_regex = re.compile(
        "|".join(signature_patterns), re.IGNORECASE | re.MULTILINE
    )

    # Search for the first occurrence of any of the signature patterns
    match = signature_regex.search(body)
    if match:
        st.info(
            "signature pattern found in the email body, delete the signature and keep the sender name"
        )

        print(f"matched with: {match.group()}")
        line_number = body[: match.start()].count("\n")
        print(f"Match found on line {line_number + 1}")

        sender_name = body[match.end() :].strip().split("\n", 1)[0]
        # If a signature is found, trim the email body up to the start of the signature
        return body[: match.start()].strip() + f"\n\n{sender_name}"
    else:
        # If no signature pattern is found, return the original email body
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
        r"^-+ Forwarded message -+$",
        r"^On \d{1,2} [A-Za-z]+ \d{4} \d{1,2}:\d{2},.* wrote:$",
    ]
    forward_regex = re.compile(
        "|".join(forward_pattern), re.IGNORECASE | re.MULTILINE
    )    

    separated_emails = re.split(forward_regex, text)
    cleaned = ""
    for mail in separated_emails:
        cleaned += remove_signature(mail)
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

    # Display your regex code
    regex_code = """
    placeholder
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

    st.title("Test Cases")

    for text in test_case():
        process_and_display(text)
        st.divider()


if __name__ == "__main__":
    main()
