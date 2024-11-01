import streamlit as st

def main():

    st.set_page_config(page_title="Harsha", page_icon="🧑‍💻", layout="wide", initial_sidebar_state="expanded", menu_items=None)

    image = "https://ibb.co/Ybm8Q57"

    col1, col2 = st.columns(2)

    with col1:
        st.image(image, width=250)

    with col2:
        st.title("Harsha Vardhan Reddy")
        st.write("Senior Software Engineer")
        st.markdown("""
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

if __name__ == "__main__":
    main()
