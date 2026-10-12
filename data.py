from models import Project, Skill, SkillLevel, NavBarItem, AboutMe, ContactInfo, SocialLink

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group / FirstWord",
        url="https://www.pslgroup.com/",
        description=(
            "I manage engineering for all of PSL Group's products in production, including FirstWord, a pharma and "
            "healthcare intelligence platform: web apps, newsletters, content feeds and an AI assistant on Bedrock."
        ),
        detailed_description=(
            "I joined as Tech Lead on FirstWord and now manage engineering for all four of our products, while "
            "still writing a lot of the code. One React codebase runs three brands, and I built FirstWord Manager, "
            "the Next.js workspace the team runs newsletters, alerts and feeds from. "
            "Behind it is a serverless TypeScript API on Lambda and DynamoDB that also powers FirstWord AI: "
            "versioned agents talking to Claude through Amazon Bedrock, with streaming, guardrails and a knowledge "
            "base. Infrastructure is Terraform and EKS with ArgoCD, deployed by shared GitHub Actions workflows I "
            "maintain."
        ),
        technologies=[
            "TypeScript",
            "Next.js",
            "React",
            "Node.js",
            "AWS",
            "Serverless",
            "Bedrock",
            "LLMs",
            "Terraform",
            "Kubernetes",
        ],
        image="psl.png",
    ),
    Project(
        title="Grupo Tress",
        url="https://www.tress.com.mx/",
        description=(
            "Built payroll software used in Mexico, the U.S. and Canada, plus the React component library behind "
            "Tress's cloud payroll product."
        ),
        detailed_description=(
            "As a Senior Developer I worked on the core apps in React, C#, Node.js, SQL and PostgreSQL, deployed on "
            "AWS, Azure and Docker. I led a self-service app where employees enroll and track their own attendance. "
            "I also built GTI Controls, the component library used by Interis Works, the company's cloud payroll "
            "system running on microservices and React. Interis Works and Sistema Tress are used by companies across "
            "Mexico, the U.S. and Canada."
        ),
        technologies=["React", "C#", "Node.js", "PostgreSQL", "AWS", "Azure"],
        image="grupotress.jpg",
    ),
    Project(
        title="Hisense México",
        url="https://www.hisense.com.mx/",
        description="Built internal tools for Hisense México's corporate offices and factory floor.",
        detailed_description=(
            "I worked in C#, ASP.NET MVC and SQL on internal projects for the corporate office and the factory. I "
            "built the IT ticketing system from scratch, worked on the corporate website, and wrote tools that "
            "connected to internal systems so managers could follow manufacturing performance in real time."
        ),
        technologies=["C#", "MVC", "SQL"],
        image="hisense.png",
        featured=False,
    ),
    Project(
        title="Umbrella Seguros",
        url="https://www.umbrella-seguros.com/",
        description="Updated an insurance management platform to make it faster and easier to use.",
        detailed_description=(
            "I worked on Umbrella's insurance platform with C#, MVC, SQL, Python and JavaScript. I rebuilt the "
            "school insurance workflows and kept extending the core features, fixing UX problems and business "
            "logic as more customers came on."
        ),
        technologies=["C#", "MVC", "SQL", "Python", "JavaScript"],
        image="umbrella.jpg",
        featured=False,
    ),
    Project(
        title="Systems Communications",
        url="https://www.systemscomm.net/es/inicio/",
        description="My internship: a truck inventory system for the Tijuana customs office.",
        detailed_description=(
            "During my internship I built an inventory system for the Tijuana customs office that logged trucks "
            "coming in and out. It was written in PHP, C# and SQL, and it was the first time something I wrote got "
            "used every day by real people."
        ),
        technologies=["PHP", "C#", "SQL"],
        image="syscoms.png",
        featured=False,
    ),
]

skills_data = [
    Skill(
        title="Engineering Management",
        icon="TbUserCode",
        description=(
            "I mentor engineers, set priorities and keep releases on schedule, and I make sure everyone knows why "
            "we're building something the way we are."
        ),
    ),
    Skill(
        title="AI & LLMs",
        icon="TbSparkles",
        description=(
            "Agents on Amazon Bedrock with Claude that ship to real users: streaming, tool use, guardrails and "
            "knowledge bases. I also roll out AI coding tools so the whole team gets faster."
        ),
    ),
    Skill(
        title="AWS & Infrastructure",
        icon="FaAws",
        description=(
            "AWS certified. Serverless on Lambda and DynamoDB, Terraform for the infrastructure, Kubernetes with "
            "ArgoCD to run it, and shared GitHub Actions so every repo deploys the same way."
        ),
    ),
    Skill(
        title="Full Stack",
        icon="SiNextdotjs",
        description=(
            "TypeScript, React, Next.js and Node.js day to day, PHP on the older services, and years of C# before "
            "that. Design systems and multi brand apps from a single codebase."
        ),
    ),
    Skill(
        title="Data & Search",
        icon="TbDatabase",
        description=(
            "DynamoDB, Aurora, MySQL and PostgreSQL for storage, OpenSearch for feeds and full text search. I model "
            "the data around how it gets read."
        ),
    ),
    Skill(
        title="Quality & Security",
        icon="TbTestPipe",
        description=(
            "Unit and end to end tests in CI, logging and error tracking from day one, and auth and secrets locked "
            "down from the start."
        ),
    ),
]

navbar_data = [
    NavBarItem(title="Home", url="/#home"),
    NavBarItem(title="About", url="/#about"),
    NavBarItem(title="Work", url="/#work"),
    NavBarItem(title="Skills", url="/#skills"),
    NavBarItem(title="Contact", url="/#contact"),
]

# the frontend splits this on blank lines, renders the first paragraph as the lead,
# and reads the "9+ years" phrase for the hero stats, so keep both shapes intact
about_me_data = AboutMe(
    title="About",
    role="Tech Lead & Engineering Manager",
    main_stack=["TypeScript", "Next.js", "React", "Node.js", "AWS", "Serverless", "Bedrock", "LLMs"],
    editor="Neovim",
    # self rated out of 5, listed by relevance: main stack, then today's tooling, then earlier stacks
    # self rated out of 5: the main stack first, then the other tools named in the work history
    skill_levels=[
        SkillLevel(name="TypeScript", level=5),
        SkillLevel(name="Next.js", level=5),
        SkillLevel(name="React", level=5),
        SkillLevel(name="Node.js", level=5),
        SkillLevel(name="AWS", level=5),
        SkillLevel(name="Serverless", level=5),
        SkillLevel(name="Bedrock", level=5),
        SkillLevel(name="LLMs", level=5),
        SkillLevel(name="C#", level=5),
        SkillLevel(name="JavaScript", level=5),
        SkillLevel(name="Terraform", level=4),
        SkillLevel(name="Kubernetes", level=4),
        SkillLevel(name="PostgreSQL", level=4),
        SkillLevel(name="SQL", level=4),
        SkillLevel(name="MVC", level=4),
        SkillLevel(name="PHP", level=4),
        SkillLevel(name="Python", level=4),
        SkillLevel(name="Azure", level=3),
    ],
    description=(
        "9+ years of building production software, from early prototypes to enterprise platforms used in "
        "three countries.\n\n"
        "I worked my way up from intern to Engineering Manager, and I've touched every layer on the way: "
        "Terraform and Kubernetes, APIs, databases and LLM integrations, up to the React screens people click "
        "on. That's why I can still go deep with anyone on the team, wherever the problem lives."
    ),
)

contact_info_data = ContactInfo(
    email="contact@cristophercervantes.com",
    mailto="mailto:contact@cristophercervantes.com",
    socials=[
        SocialLink(
            id=1, name="LinkedIn", url="https://www.linkedin.com/in/thecristopher/"
        ),
        SocialLink(
            id=2, name="GitHub", url="https://github.com/thecristopher"
        ),
        SocialLink(
            id=3, name="Instagram", url="https://www.instagram.com/thecristopher/"
        ),
    ],
)
