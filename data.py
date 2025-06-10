from models import Project, Skill

# Data for the portfolio projects and skills
project_data = [
    Project(
        name="PSL Group / FirstWord",
        description="Delivered scalable pharma insights through modern web apps & feed infrastructure.",
        url="https://www.pslgroup.com/",
        technologies=["React", "PHP", "AWS", "Docker", "Node.js", "MySQL", "PostgreSQL"]
    ),
    Project(
        name="Grupo Tress",
        description="Built enterprise-grade payroll tools with secure, high-performance architecture.",
        url="http://tress.com.mx/",
        technologies=["React", "AWS", "C#", "docker", "Node.js", ".NET", "SQL Server", "PostgreSQL"] 
    )
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
