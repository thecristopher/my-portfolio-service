from models import Project, Skill

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group / FirstWord",
        url="https://www.pslgroup.com/",
        description="Delivered scalable pharma insights through modern web apps & feed infrastructure.",
        technologies=["React", "PHP", "Python", "AWS", "Docker", "Node.js", "MySQL", "PostgreSQL"],
        image="psl.png"
    ),
    Project(
        title="Grupo Tress",
        url="https://www.tress.com.mx/",
        description="Built enterprise-grade payroll tools with secure, high-performance architecture.",
        technologies=["React", "C#", "AWS", "Azure", "Docker", "Node.js", "SQL", "PostgreSQL"],
        image="grupotress.jpg"
    ),
    Project(
        title="Hisense México",
        url="https://www.hisense.com.mx/",
        description="Developed corporate & factory tooling for productivity and systems integration.",
        technologies=["C#", "MVC", "SQL"],
        image="hisense.png"
    ),
    Project(
        title="Umbrella Seguros",
        url="https://www.umbrella-seguros.com/",
        description="Built modern insurance platform focused on speed, UX, and digital reach.",
        technologies=["C#", "MVC", "SQL", "Python", "JavaScript"],
        image="umbrella.jpg"
    ),
    Project(
        title="Genesis Cazares, DDS",
        url="https://dentistagenesiscazares.com",
        description="Promoted services through a responsive C# MVC web app tailored for visibility.",
        technologies=["C#", "MVC", "SQL", "JavaScript"],
        image="dentist_genesis.png"
    ),
]

skills_data = [
    Skill(
        title="Fullstack Development",
        icon="TbUserCode",
        description="I craft systems that connect frontend and backend seamlessly, focusing on speed, maintainability, and user experience — regardless of the stack."
    ),
    Skill(
        title="Cloud Infrastructure",
        icon="FaAws",
        description="With AWS and DevOps know-how, I ship scalable and production-ready systems that run smoothly and securely at any scale."
    ),
    Skill(
        title="Frontend",
        icon="FaReact",
        description="Beyond React, I focus on creating intuitive interfaces that scale with your users — blending design, accessibility, and performance."
    ),
    Skill(
        title="Creative Design",
        icon="PiPaintBrushBroadBold",
        description="From motion graphics to UI aesthetics, I turn ideas into visual experiences that resonate with users and elevate brands."
    ),
    Skill(
        title="Web Craftsmanship",
        icon="FaJsSquare",
        description="My foundation in JavaScript and browser tech allows me to optimize, modernize, and enhance any web experience — with or without frameworks."
    ),
    Skill(
        title="App Security & Observability",
        icon="GrShieldSecurity",
        description="Performance and trust go hand in hand. I implement analytics, error tracking, and security patterns to ensure stability and insight."
    ),
]
