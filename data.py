from models import Project, Skill, NavBarItem, AboutMe, ContactInfo, SocialLink

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group / FirstWord",
        url="https://www.pslgroup.com/",
        description="Delivered scalable pharma and medical insights through modern web apps, newsletters, feed infrastructure and AI models.",
        detailed_description=(
            "As the Tech Lead for the FirstWord application, I oversee all technology decisions that keep our platform at the forefront of modern SaaS standards. "
            "Utilizing technologies like React, PHP, Python, AWS, Docker, Node.js, MySQL, and PostgreSQL, I deliver a scalable, intelligent platform that lets users "
            "browse applications, read newsletters, and request more insights — all enhanced by a custom-built AI model. My AWS certifications support daily tasks of "
            "diagnosing issues, proposing solutions, and evolving PSL’s suite of tools."
        ),
        technologies=[
            "React",
            "PHP",
            "Python",
            "AWS",
            "Docker",
            "Node.js",
            "MySQL",
            "PostgreSQL",
        ],
        image="psl.png",
    ),
    Project(
        title="Grupo Tress",
        url="https://www.tress.com.mx/",
        description="Built enterprise-grade payroll tools with secure, high-performance architecture.",
        detailed_description=(
            "As a Senior Developer, I maintained and expanded core applications within Grupo Tress Internacional using React, C#, AWS, Azure, Docker, Node.js, SQL, and PostgreSQL. "
            "I led the development of a self-enrollment payroll application that empowered users to manage check-ins and outs. Additionally, I designed GTI Controls — a reusable UI component "
            "library powering 'Interis Works', a cloud-based payroll system built with microservices and React. Together with Sistema Tress, this platform stands as a pioneer in payroll software across Mexico, the U.S., and Canada."
        ),
        technologies=[
            "React",
            "C#",
            "AWS",
            "Azure",
            "Docker",
            "Node.js",
            "SQL",
            "PostgreSQL",
        ],
        image="grupotress.jpg",
    ),
    Project(
        title="Hisense México",
        url="https://www.hisense.com.mx/",
        description="Developed corporate & factory tooling for productivity and systems integration.",
        detailed_description=(
            "With C#, MVC, and SQL, I spearheaded several projects to boost productivity across Hisense Mexico's corporate and factory environments. "
            "This included a ticketing system for IT requests built from scratch and contributions to the official corporate website. "
            "My tools helped streamline manufacturing performance, integrating with internal systems for real-time improvements."
        ),
        technologies=["C#", "MVC", "SQL"],
        image="hisense.png",
    ),
    Project(
        title="Umbrella Seguros",
        url="https://www.umbrella-seguros.com/",
        description="Built modern insurance platform focused on speed, UX, and digital reach.",
        detailed_description=(
            "I enhanced and modernized Umbrella’s insurance management platform, using technologies like C#, MVC, SQL, Python, and JavaScript. "
            "Beyond revamping school insurance workflows, I maintained and extended core features, improving UI/UX and operational logic to scale with user needs."
        ),
        technologies=["C#", "MVC", "SQL", "Python", "JavaScript"],
        image="umbrella.jpg",
    ),
     Project(
        title="Systems Communications",
        url="https://www.systemscomm.net/es/inicio/",
        description="Learned clean code principles while creating automated systems for transportation and inventory management.",
        detailed_description=(
            "During my internship, I put clean code principles into practice by developing a transportation inventory system used by the Tijuana customs office. "
            "Using PHP, C#, and SQL, I created a tool for tracking truck check-ins and check-outs, supporting logistics in a real-world, high-volume environment."
        ),
        technologies=["PHP", "C#", "SQL"],
        image="syscoms.png",
    ),
]

skills_data = [
    Skill(
        title="Fullstack Development",
        icon="TbUserCode",
        description="I craft systems that connect frontend and backend seamlessly, focusing on speed, maintainability, and user experience — regardless of the stack.",
    ),
    Skill(
        title="Cloud Infrastructure",
        icon="FaAws",
        description="With AWS and DevOps know-how, I ship scalable and production-ready systems that run smoothly and securely at any scale.",
    ),
    Skill(
        title="Frontend",
        icon="FaReact",
        description="Beyond React, I focus on creating intuitive interfaces that scale with your users — blending design, accessibility, and performance.",
    ),
    Skill(
        title="Creative Design",
        icon="PiPaintBrushBroadBold",
        description="From motion graphics to UI aesthetics, I turn ideas into visual experiences that resonate with users and elevate brands.",
    ),
    Skill(
        title="Web Craftsmanship",
        icon="FaJsSquare",
        description="My foundation in JavaScript and browser tech allows me to optimize, modernize, and enhance any web experience — with or without frameworks.",
    ),
    Skill(
        title="App Security & Observability",
        icon="GrShieldSecurity",
        description="Performance and trust go hand in hand. I implement analytics, error tracking, and security patterns to ensure stability and insight.",
    ),
]

navbar_data = [
    NavBarItem(title="Home", url="/#home"),
    NavBarItem(title="About", url="/#about"),
    NavBarItem(title="Work", url="/#work"),
    NavBarItem(title="Skills", url="/#skills"),
    NavBarItem(title="Contact", url="/#contact"),
]

about_me_data = AboutMe(
    title="About",
    description=(
        "Hey there! I’m Cristopher Cervantes, a fullstack developer with 9+ years of experience crafting everything from quick prototypes to enterprise-grade systems. I bridge the gap between front-end finesse and back-end muscle.\n\n"
        'Throughout my career, I’ve had the chance to work with companies that didn’t just need "a developer," but someone who could jump between stacks, tackle legacy obstacles, and still deliver clean, scalable code. From building PHP-based platforms to wrangling cloud-native APIs with Python, I’ve pretty much been everywhere.\n\n'
        "I'm fluent in several tech dialects: C#, .NET, React, PHP, Python, Node.js — you name it. Databases? Oh yeah. Whether it's MySQL, PostgreSQL, or NoSQL flavors, I love getting into data structure debates.\n\n"
        "I’m also officially AWS-certified — both as a Cloud Practitioner and a Developer Associate. Translation: I can launch, scale, and troubleshoot your cloud infrastructure before my second cup of coffee.\n\n"
        "At the core of it all, I’m someone who loves learning, building, and solving the kind of problems that make other developers sigh dramatically. I’m always up for a challenge — especially the kind that lets me push tech boundaries while having a good laugh in the process."
    ),
)

contact_info_data = ContactInfo(
    email="isc.cristopher@gmail.com",
    mailto="mailto:isc.cristopher@gmail.com",
    socials=[
        SocialLink(
            id=1, name="LinkedIn", url="https://www.linkedin.com/in/thecristopher/"
        ),
        SocialLink(
            id=2, name="YouTube", url="https://www.youtube.com/@thecristopherofficial"
        ),
        SocialLink(
            id=3, name="Instagram", url="https://www.instagram.com/thecristopher/"
        ),
        SocialLink(
            id=4, name="TikTok", url="https://www.tiktok.com/@thecristopherofficial"
        ),
        SocialLink(
            id=5, name="Twitch", url="https://www.twitch.tv/thecristopherofficial"
        ),
    ],
)
