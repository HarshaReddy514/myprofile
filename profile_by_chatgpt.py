import streamlit as st

from PIL import Image

def main():

    image = Image.open("https://github.com/HarshaReddy514/myprofile/blob/main/Harsha.jpg")

    st.image(image, width=300)

    st.title("Harsha Vardhan Reddy")
    st.subheader("Senior Software Engineer")

    st.sidebar.markdown('''
- [LinkedIn](https://www.linkedin.com/in/harshavardhanreddy-bommareddy/)
- [Medium](https://harshavardhan-reddy.medium.com)
''', unsafe_allow_html=True)

    # Education Section
    st.header("Education")
    st.write("Jawaharlal Nehru Technological University - Kakinada")
    st.write("B. Tech in Computer Science and Engineering (Percentage: 73)")

    # Work Experience Section
    st.header("Work Experience")

    # Altimetrik India Private Limited
    st.subheader("Altimetrik India Private Limited")
    st.write("Senior Engineer")
    st.write("Location: Tadepalligudem – Andhra Pradesh (Graduation Month/Year: April 2016)")
    st.write("Location: Chennai - Tamil Nadu (September 2021 – Present)")
    st.write("- Working on fixing a major issue in Hyperwallet disabled cards balance")
    st.write("- Implemented JWT Sign and Verification for PayPal IVS Component")
    st.write("- Implemented web alerts for negative balance users in notifications service")
    st.write("- Worked on improving PPC FT Coverage for DebtProfileServ and RBO Validation in PlacementServ")

    # Valeo India Private Limited
    st.subheader("Valeo India Private Limited")
    st.write("Senior Engineer (April 2021 - September 2021)")
    st.write("- Worked on a supply chain management application and pushed the application to production")
    st.write("- Worked on a complex requirement which predominantly is on UI part and implemented a logic which reduces cost on a cron job read and write operations")
    st.write("- Volunteered to take responsibility for training Java interns")

    st.write("Engineer (August 2019 - April 2021)")
    st.write("- Delivered bug-free release of IC Non-Trade Contract Management application")
    st.write("- Fixed an issue on reading the data from PDF invoices using OCR")

    # Full Creative Private Limited
    st.subheader("Full Creative Private Limited")
    st.write("Junior Software Engineer (October 2016 - August 2019)")
    st.write("- Contributed as an individual to build a chrome extension for YoCoBoard (A time tracking app)")
    st.write("- Improved the load time on the hours page")
    st.write("- Recognized as a useful resource to work on fixing production issues in Setmore – Appointment scheduling application")

    st.write("Java Intern (June 2016 - September 2016)")
    st.write("- Joined Full Creative as a Java intern")
    st.write("- Upskilled on Java and learned Spring, JavaScript, jQuery, HTML, CSS, AJAX, JSON, and Git")
    st.write("- Was in an Edu Scrum team of four members")
    st.write("- Developed two web applications: FeedSystem to share multiple user’s feeds and a Q/A forum to post and answer questions")

    # Skills Section
    st.header("Skills")
    st.write("Java, Spring Boot, JavaScript, jQuery, JSON, Ajax, HTML, CSS, JUnit, Mockito, Power Mock, Google App Engine, Datastore, Cloud Tasks, Cron Scheduler, Agile Methodologies")

    # Certifications Section
    st.header("Certifications")
    st.write("- Oracle Certified Professional - Java SE 6 Programmer")
    st.write("- edX Honor Code Certificate for Introduction to Mobile Application Development using Android")

if __name__ == "__main__":
    main()
