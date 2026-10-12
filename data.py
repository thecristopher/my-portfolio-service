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

# attack, defense and effect only show once Dark Magician Girl buffs the page and every card becomes a duel monster
skills_data = [
    Skill(
        title="Leading Teams",
        icon="TbUserCode",
        description=(
            "I mentor engineers, run 1:1s and code reviews, set priorities and keep releases on a steady schedule. "
            "I'd rather unblock five people than write the clever thing myself."
        ),
        attack=2500,
        defense=2100,
        effect="Once per sprint: every engineer on your side of the field is unblocked.",
    ),
    Skill(
        title="AI & LLMs",
        icon="TbSparkles",
        description=(
            "LLM features are still features: they need guardrails, tests and a fallback for when the model gets it "
            "wrong. I've shipped AI that people use every day, and I'd take a boring correct answer over a flashy "
            "wrong one."
        ),
        attack=2800,
        defense=1700,
        effect="When a model hallucinates, negate it and return a grounded answer instead.",
    ),
    Skill(
        title="Cloud & Infra",
        icon="FaAws",
        description=(
            "Functions when traffic is spiky, containers when it isn't. Every environment lives in code and every "
            "repo ships through the same pipeline, so deploys are boring in the best way."
        ),
        attack=2300,
        defense=2800,
        effect="Cannot be destroyed by a Friday deploy.",
    ),
    Skill(
        title="Frontend & UX",
        icon="TbLayoutDashboard",
        description=(
            "Design systems and component libraries a whole product, or several brands, can share. I sweat the small "
            "stuff too: loading states, dark mode, i18n and copy that sounds like a person wrote it."
        ),
        attack=2400,
        defense=2000,
        effect="Flip every loading spinner on the field into a skeleton.",
    ),
    Skill(
        title="Data & Search",
        icon="TbDatabase",
        description=(
            "I model data around how it gets read, then make sure the indexes agree. NoSQL when the access patterns "
            "are known, SQL when the data has real relationships, and a search engine when people need to find "
            "things fast."
        ),
        attack=2200,
        defense=2500,
        effect="Search your deck for any record and add it to your hand. Indexed, of course.",
    ),
    Skill(
        title="Quality & Security",
        icon="TbTestPipe",
        description=(
            "Unit tests for the logic, end to end tests for the flows people actually click, and CI that blocks the "
            "merge when they fail. Logging, alerts and locked down secrets go in before launch, not after the first "
            "incident."
        ),
        attack=1900,
        defense=3000,
        effect="Negate any attack that skipped CI.",
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
        "I started as an intern and worked my way up through senior developer and tech lead to engineering "
        "manager. So I can still pair on a gnarly bug, review a pull request line by line or sketch the "
        "architecture, then go sort out the roadmap.\n\n"
        "I explain every tradeoff so nobody has to guess why we built something the way we did, and I aim for "
        "code the next engineer can pick up on their own.\n\n"
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
