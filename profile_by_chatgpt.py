import streamlit as st

from PIL import Image

def main():

    st.set_page_config(page_title="Harsha Vardhan Reddy", page_icon="🧑‍💻", layout="centered", initial_sidebar_state="auto", menu_items=None)

    image = "https://media.licdn.com/dms/image/D5603AQFSvTxudNDn1Q/profile-displayphoto-shrink_800_800/0/1633344799157?e=1711584000&v=beta&t=MQ3QWWgYwXQ-2rVFliVK87a-6M1LYKk995hpPwbLxOE"
    st.image(image, width=300)

    st.title("Harsha Vardhan Reddy")
    st.subheader("Senior Software Engineer")

    st.sidebar.markdown('''
- [LinkedIn](https://www.linkedin.com/in/harshavardhanreddy-bommareddy/)
- [Medium](https://harshavardhan-reddy.medium.com)
''', unsafe_allow_html=True)

    st.markdown("""
    ## Experienced IT Professional with a Passion for Innovation

    Welcome to my corner of the digital realm! With 7 years in the IT industry, I've honed my skills as a tech enthusiast and problem solver. My journey has been fueled by a relentless curiosity and a commitment to staying at the forefront of technological advancements.
    """)

    st.markdown("### Technical Expertise:")
    st.markdown("""
    - **Programming Languages:** Proficient in Java and Python, I thrive in crafting robust and scalable solutions.
    - **Frameworks:** Specializing in Spring Boot and Microservices architecture, I bring a wealth of experience in developing and optimizing high-performance applications.
    - **Cloud Technologies:** Well-versed in cutting-edge cloud technologies, I seamlessly navigate through the digital clouds to ensure efficient and scalable solutions.
    - **Version Control and Tools:** GitHub is my second home, and I wield tools like IntelliJ and Eclipse with finesse, ensuring a seamless development experience.
    """)

    st.markdown("### Why Choose Me:")
    st.markdown("""
    In a rapidly evolving tech landscape, adaptability is key. I not only bring a solid foundation built on years of experience but also a commitment to continuous learning. Whether it's troubleshooting complex issues or architecting innovative solutions, I thrive on the challenges that come my way.
    """)

    st.markdown("### Beyond the Code:")
    st.markdown("""
    My journey is not just about lines of code. It's about collaborating, problem-solving, and adding real value to every project I undertake. Let's not just meet expectations; let's exceed them together.
    """)

    st.markdown("### Let's Connect:")
    st.markdown("""
    Explore the possibilities of what we can achieve together. Whether you're looking to streamline your development process, troubleshoot a challenging issue, or embark on a new project, I'm ready to be your tech partner.

    Feel free to reach out, and let's turn your tech visions into reality.
    """)

if __name__ == "__main__":
    main()
