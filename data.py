from models import (
    AboutMe,
    Certification,
    ContactInfo,
    Education,
    NavBarItem,
    Project,
    Skill,
    SkillLevel,
    SocialLink,
)

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group",
        url="https://www.pslgroup.com/",
        description=(
            "I run engineering for four of PSL Group's products: DGPL, AMI, IDH and MEC. I set the priorities, lead "
            "the team and still review and write plenty of the code."
        ),
        # the frontend splits this on blank lines, one paragraph per chapter of the role
        detailed_description=(
            "I joined as Tech Lead on FirstWord, PSL's pharma and healthcare intelligence platform, and grew into "
            "managing engineering across the group's products.\n\n"
            "On FirstWord I built one React codebase serving three brands, FirstWord Manager (the Next.js workspace "
            "the team runs everything from) and FirstWord AI, versioned Claude agents on Bedrock with streaming and "
            "guardrails.\n\n"
            "Today I split my week between product and code: planning the roadmap for DGPL, AMI, IDH and MEC, running "
            "1:1s, and pushing back on pull requests with alternatives until the team lands something better. I also "
            "own the shared deploy pipelines and the infrastructure as code, and set up the Claude Code tooling the "
            "whole team works with."
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
            "Lambda",
            "DynamoDB",
            "Aurora",
            "OpenSearch",
            "Terraform",
            "Kubernetes",
            "GitHub Actions",
            "PHP",
        ],
        image="psl.png",
    ),
    Project(
        title="Grupo Tress",
        url="https://www.tress.com.mx/",
        description=(
            "Payroll and HR software used by companies across Mexico, the U.S. and Canada. I joined as a developer "
            "and grew into a Senior Developer leading features end to end."
        ),
        detailed_description=(
            "As Senior Developer I led the self service app where employees track their own attendance, owning it "
            "from the first screens to production.\n\n"
            "I also built GTI Controls, the React component library behind Interis Works, Tress's cloud payroll "
            "product, so every team shipped screens that looked and behaved the same.\n\n"
            "Along the way I worked across the C# and Node.js services, the PostgreSQL databases and the cloud "
            "deployments on AWS and Azure."
        ),
        technologies=["React", "C#", "Node.js", "PostgreSQL", "SQL", "AWS", "Azure", "Docker"],
        image="grupotress.jpg",
    ),
    Project(
        title="Hisense México",
        url="https://www.hisense.com.mx/",
        description="Internal tools for the corporate office and the factory floor, including the IT ticketing system.",
        detailed_description=(
            "I built the IT ticketing system from scratch in C#, ASP.NET MVC and SQL, and it became how the whole "
            "office asked for help.\n\n"
            "I also worked on the corporate website and wrote tools that connected to internal systems so managers "
            "could follow manufacturing performance in real time."
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
            "school insurance workflows from the ground up.\n\n"
            "As more customers came on I kept extending the core features, fixing UX problems and tightening the "
            "business logic so the platform could grow with them."
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
            "coming in and out, written in PHP, C# and SQL.\n\n"
            "It was the first time something I wrote got used every day by real people, and the reason I never "
            "looked back."
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
    NavBarItem(title="Education", url="/#education"),
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
        SkillLevel(name="Lambda", level=5),
        SkillLevel(name="DynamoDB", level=5),
        SkillLevel(name="Aurora", level=4),
        SkillLevel(name="OpenSearch", level=4),
        SkillLevel(name="Terraform", level=4),
        SkillLevel(name="Kubernetes", level=4),
        SkillLevel(name="GitHub Actions", level=4),
        SkillLevel(name="Docker", level=4),
        SkillLevel(name="PostgreSQL", level=4),
        SkillLevel(name="SQL", level=4),
        SkillLevel(name="MVC", level=4),
        SkillLevel(name="PHP", level=4),
        SkillLevel(name="Python", level=4),
        SkillLevel(name="Azure", level=3),
    ],
    education=[
        Education(
            school="Instituto Tecnológico de Tijuana",
            url="https://www.tijuana.tecnm.mx/",
            location="Tijuana, Mexico",
            degree="B.S. in Computer Systems Engineering",
            original_name="Ingeniería en Sistemas Computacionales",
            highlights=[
                "Where I learned the fundamentals I still lean on: algorithms, data structures, databases, networks "
                "and software engineering.",
                "Part of TecNM, Mexico's national network of public engineering schools.",
            ],
        ),
    ],
    certifications=[
        Certification(name="AWS Certified Developer \u2013 Associate", issuer="Amazon Web Services", level="Associate"),
        Certification(name="AWS Certified Cloud Practitioner", issuer="Amazon Web Services", level="Foundational"),
    ],
    description=(
        "I started like everyone else, as an intern who could barely scratch out a few lines of code. Over 9+ "
        "years I climbed one step at a time, until I became one of the key developers at every company I've "
        "worked for.\n\n"
        "I challenge myself every day and I'm always after continuous improvement, both in myself and in the "
        "products I help build.\n\n"
        "Today I'm a mix of Engineering Manager and Tech Lead. I don't just set the priorities for my products, I "
        "also suggest alternatives and solutions to the code my developers propose, and push them so that "
        "together we always land a better result.\n\n"
        "Off the clock I love working out, spending time with my family, and every now and then reading some "
        "manga or playing video games. By the way, have you tried finding the easter eggs scattered around here?"
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
