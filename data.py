from models import Project, Skill, NavBarItem, AboutMe, ContactInfo, SocialLink

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group / FirstWord",
        url="https://www.pslgroup.com/",
        description="Delivered scalable pharma and medical insights through modern web apps, newsletters, feed infrastructure and AI models.",
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
        technologies=["C#", "MVC", "SQL"],
        image="hisense.png",
    ),
    Project(
        title="Umbrella Seguros",
        url="https://www.umbrella-seguros.com/",
        description="Built modern insurance platform focused on speed, UX, and digital reach.",
        technologies=["C#", "MVC", "SQL", "Python", "JavaScript"],
        image="umbrella.jpg",
    ),
     Project(
        title="Systems Communications",
        url="https://www.systemscomm.net/es/inicio/",
        description="Learned clean code principles while creating automated systems for transportation and inventory management.",
        technologies=["PHP", "C#", "SQL"],
        image="systemscommunications.png",
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
