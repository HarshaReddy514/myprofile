import streamlit as st

def main():

    st.set_page_config(page_title="Harsha", page_icon="🧑‍💻", layout="wide", initial_sidebar_state="expanded", menu_items=None)
    
    st.subheader("Harsha Vardhan Reddy")
    st.write("Designation : Senior Software Engineer")
    st.write("E-Mail : harshavardhan.samba@gmail.com")

    # Education Section
    st.subheader("Education")
    st.write("Jawaharlal Nehru Technological University - Kakinada")
    st.write("Bachelor of Technology in Computer Science and Engineering (Percentage: 73)")
    st.write("Location: Tadepalligudem – Andhra Pradesh (Graduation Month/Year: April 2016)")

    # Work Experience Section
    st.subheader("Work Experience")

    # Altimetrik India Private Limited
    st.write("**Altimetrik India Private Limited - Senior Engineer (September 2021 – Present)**")
    st.write("Location: Chennai - Tamil Nadu")
    st.write("- Working on fixing a major issue in Hyperwallet disabled cards balance")
    st.write("- Implemented JWT Sign and Verification for PayPal IVS Component")
    st.write("- Implemented web alerts for negative balance users in notifications service")
    st.write("- Worked on improving PPC FT Coverage for DebtProfileServ and RBO Validation in PlacementServ")

    # Valeo India Private Limited
    st.write("**Valeo India Private Limited - Senior Engineer (April 2021 - September 2021)**")
    st.write("- Worked on a supply chain management application and pushed the application to production")
    st.write("- Worked on a complex requirement which predominantly is on UI part and implemented a logic which reduces cost on a cron job read and write operations")
    st.write("- Volunteered to take responsibility for training Java interns")

    st.write("**Engineer (August 2019 - April 2021)**")
    st.write("- Delivered bug-free release of IC Non-Trade Contract Management application")
    st.write("- Fixed an issue on reading the data from PDF invoices using OCR")

    # Full Creative Private Limited
    st.write("**Full Creative Private Limited - Junior Software Engineer (October 2016 - August 2019)**")
    st.write("- Contributed as an individual to build a chrome extension for YoCoBoard (A time tracking app)")
    st.write("- Improved the load time on the hours page")
    st.write("- Recognized as a useful resource to work on fixing production issues in Setmore – Appointment scheduling application")

    st.write("**Java Intern (June 2016 - September 2016)**")
    st.write("- Joined Full Creative as a Java intern")
    st.write("- Upskilled on Java and learned Spring, JavaScript, jQuery, HTML, CSS, AJAX, JSON, and Git")
    st.write("- Was in an Edu Scrum team of four members")
    st.write("- Developed two web applications: FeedSystem to share multiple user’s feeds and a Q/A forum to post and answer questions")

    # Skills Section
    st.subheader("Skills")
    st.write("Java, Spring Boot, JavaScript, jQuery, JSON, Ajax, HTML, CSS, JUnit, Mockito, Power Mock, Google App Engine, Datastore, Cloud Tasks, Cron Scheduler, Agile Methodologies")

    # Certifications Section
    st.subheader("Certifications")
    st.write("- Oracle Certified Professional - Java SE 6 Programmer")
    st.write("- edX Honor Code Certificate for Introduction to Mobile Application Development using Android")

if __name__ == "__main__":
    main()
