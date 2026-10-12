from models import Project, Skill, SkillLevel, NavBarItem, AboutMe, ContactInfo, SocialLink

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group / FirstWord",
        url="https://www.pslgroup.com/",
        description=(
            "I run engineering for PSL Group's four products. The big one is FirstWord, pharma and healthcare "
            "intel served as web apps, newsletters, feeds and an AI assistant."
        ),
        detailed_description=(
            "Joined as Tech Lead and grew into managing the team. Highlights: one "
            "React codebase serving three brands, FirstWord Manager (the Next.js workspace the team runs everything "
            "from) and FirstWord AI, versioned Claude agents on Bedrock with streaming and guardrails. I also own "
            "the shared deploy pipelines and set up the Claude Code tooling the whole team uses."
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
        description="Payroll software used by companies across Mexico, the U.S. and Canada.",
        detailed_description=(
            "As Senior Developer I led a self service app where employees track their own attendance, and built GTI "
            "Controls, the React component library behind Interis Works, Tress's cloud payroll product."
        ),
        technologies=["React", "C#", "Node.js", "PostgreSQL", "AWS", "Azure"],
        image="grupotress.jpg",
    ),
    Project(
        title="Hisense México",
        url="https://www.hisense.com.mx/",
        description="Internal tools for the office and factory floor, including the IT ticketing system.",
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
        description="Rebuilt the school insurance workflows on their management platform.",
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
        description="Internship. Built the truck log for the Tijuana customs office, my first code in daily use.",
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
        title="Leading Teams",
        icon="TbUserCode",
        description=(
            "1:1s, code reviews and release planning. I'd rather unblock five people than write the clever thing "
            "myself."
        ),
    ),
    Skill(
        title="AI & LLMs",
        icon="TbSparkles",
        description=(
            "LLM features are still features: they need guardrails, tests and a way to roll back. No demo magic "
            "that falls over in production."
        ),
    ),
    Skill(
        title="Cloud & Infra",
        icon="FaAws",
        description=(
            "Functions when traffic is spiky, containers when it isn't, and all of it in code so nobody is "
            "clicking around a console."
        ),
    ),
    Skill(
        title="Frontend & UX",
        icon="TbLayoutDashboard",
        description=(
            "I sweat the small stuff: loading states, dark mode, i18n and copy that sounds like a person wrote it."
        ),
    ),
    Skill(
        title="Data & Search",
        icon="TbDatabase",
        description=(
            "Model the data around how it gets read, then make sure the indexes agree. NoSQL when the access "
            "patterns are known, SQL when the data has real relationships."
        ),
    ),
    Skill(
        title="Quality & Security",
        icon="TbTestPipe",
        description=(
            "Tests are how the next engineer trusts my code. CI blocks the merge, alerts exist before launch and "
            "secrets never live in the repo."
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
        "9+ years of shipping software taught me the code is the easy part. The hard part is a team that knows "
        "what to build and why.\n\n"
        "Off the clock it's video games and anime, which might explain a few things hidden around this page."
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
