from models import (
    AboutMe,
    CaseStudy,
    Certification,
    ContactInfo,
    Education,
    Language,
    Metric,
    NavBarItem,
    Project,
    Skill,
    SkillLevel,
    SocialLink,
)

# every place I've worked, newest first. the description says what the company does, the highlights say what I
# did there, and anything with a case study of its own is told once, over in case_studies_data
projects_data = [
    Project(
        title="PSL Group",
        roles=["Senior Application Developer", "Tech Lead", "Engineering Manager"],
        url="https://www.pslgroup.com/",
        description="Medical and pharma news, read by professionals all over the world.",
        highlights=[
            "Joined to keep FirstWord, PSL's medical news platform, fast and current for readers worldwide",
            "Now run engineering for FirstWord, DGPL, MEC, AMI and the rest of PSL's product line",
            "Plan the roadmap, run the 1:1s and still ship code most weeks",
        ],
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
    ),
    Project(
        title="Grupo Tress Internacional",
        roles=["Developer", "Senior Developer"],
        url="https://www.tress.com.mx/",
        description="Payroll and HR software that companies in Mexico, the U.S. and Canada run their people on.",
        highlights=[
            "Worked on the +orden console and Interis Works, the payroll products Tress customers use every pay period",
            "Moved across C# and Node.js services, PostgreSQL and deployments on both AWS and Azure",
        ],
        technologies=["React", "C#", "Node.js", "PostgreSQL", "SQL", "AWS", "Azure", "Docker"],
    ),
    Project(
        title="Hisense",
        url="https://www.hisense.com.mx/",
        description="The TV and appliance maker. I worked where the software meets the factory floor.",
        highlights=[
            "Worked on the corporate website between plant projects",
        ],
        technologies=["C#", "MVC", "SQL"],
        featured=False,
    ),
    Project(
        title="Umbrella Seguros",
        url="https://www.umbrella-seguros.com/",
        description="An insurance company, and the one admin app both its staff and its policyholders log into.",
        highlights=[
            "One of the lead developers of Umbrella's admin app, an Azure client for the insurer and the insured alike",
            "Rebuilt the school insurance workflows from the ground up",
        ],
        technologies=["C#", "MVC", "SQL", "Python", "JavaScript", "Azure"],
        note="Gracias a Erika Soto por la confianza y por todo lo que me enseñó.",
        featured=False,
    ),
    Project(
        title="Systems Communications",
        roles=["Intern"],
        url="https://www.systemscomm.net/es/inicio/",
        description="Where I wrote my first line of production code, for the people who run the border.",
        highlights=[
            "Maintained the app CBP used to control customs access and inspect trailers and commercial trucks",
            "Learned PHP and C# on a system the border couldn't afford to have down",
        ],
        technologies=["PHP", "C#", "SQL"],
        featured=False,
    ),
]

# the work I'd walk a hiring manager through, told as what was hard, what I did and what changed.
# metrics only go in when someone actually measured them
case_studies_data = [
    CaseStudy(
        slug="firstword-ai",
        title="FirstWord AI",
        company="PSL Group",
        role="Tech Lead",
        kind="AI",
        summary="Claude agents on AWS Bedrock that answer questions about the medical news FirstWord publishes.",
        challenge=(
            "FirstWord's readers make real decisions on what they read. An assistant that sounds sure and gets it "
            "wrong would cost more trust than it could ever earn."
        ),
        approach=[
            "Versioned every agent, so a prompt or model change ships and rolls back like any other release",
            "Streamed answers to the reader while the model is still writing, nobody stares at a spinner",
            "Put guardrails in front of every response, and kept the model honest with tests",
        ],
        outcome="An assistant that lives inside the product readers already open every day, not off to the side of it.",
        technologies=["TypeScript", "Bedrock", "LLMs", "Lambda", "Serverless", "React"],
    ),
    CaseStudy(
        slug="firstword-manager",
        title="FirstWord Manager",
        company="PSL Group",
        role="Tech Lead",
        kind="Platform",
        summary="The workspace the FirstWord team runs its day from, with the information in one place and the busywork on autopilot.",
        challenge="What the team needed lived across several tools, and a good part of every week went to repeating the same steps by hand.",
        approach=[
            "Built FirstWord Manager in Next.js, the one workspace the team runs everything from",
            "Centralized the information that was spread across tools, so everyone works from the same source",
            "Automated the processes the team used to run by hand",
        ],
        outcome="Less time hunting for data and repeating steps, more time on the work that actually moves FirstWord forward.",
        technologies=["Next.js", "React", "TypeScript", "Node.js"],
    ),
    CaseStudy(
        slug="shared-pipelines",
        title="Pipelines every team ships through",
        company="PSL Group",
        role="Engineering Manager",
        kind="Platform",
        summary="One road to production for every repo, plus the Claude Code setup the whole team works with.",
        challenge="Every repo deployed its own way, which made releases slow to review and nerve wracking to press.",
        approach=[
            "Moved the environments into infrastructure as code",
            "Wrote shared GitHub Actions workflows that every repo reuses instead of copying",
            "Set up Claude Code and the conventions around it, so the team gets help without losing its own style",
        ],
        outcome="A new repo is ready to ship on day one, through the same reviewed path as every other.",
        technologies=["Terraform", "GitHub Actions", "AWS", "Kubernetes", "Serverless"],
    ),
    CaseStudy(
        slug="gti-terminals",
        title="GTI B2 and facial terminals",
        company="Grupo Tress Internacional",
        role="Senior Developer",
        kind="Product",
        summary="Attendance terminals, including facial ones, that Tress customers leaned on to keep track of their people through the pandemic.",
        challenge="Companies still needed to know who was at work, in the middle of a pandemic.",
        approach=[
            "Built the GTI B2 terminals, and then the facial terminals that followed them",
        ],
        outcome="Some of the first tools Tress customers had for personnel control during the pandemic.",
        technologies=[],
    ),
    CaseStudy(
        slug="gti-controls",
        title="GTI Controls",
        company="Grupo Tress Internacional",
        role="Senior Developer",
        kind="Frontend",
        summary="The React component library under Interis Works, Tress's cloud payroll product.",
        challenge="Several teams were building one product, and you could tell which team built which screen.",
        approach=[
            "Built one shared library of React components for the whole product",
            "Gave every team the same building blocks for forms, tables and layouts",
        ],
        outcome="You can no longer tell which team built which screen, which was the whole point.",
        technologies=["React", "JavaScript", "Node.js"],
    ),
    CaseStudy(
        slug="hisense-plant",
        title="A plant that doubled its output",
        company="Hisense",
        role="Developer",
        kind="Product",
        summary="Software that talked straight to the factory robots, and took a whole plant's productivity up 100%.",
        challenge="Material, people and machines on the plant floor were coordinated by hand, and it showed in the numbers.",
        approach=[
            "Designed automated processes that talk directly to the plant's robotics",
            "Added material access and personnel control to the same system",
            "Built a Jira style ticketing app so the IT team could stop living in email",
        ],
        outcome="Plant productivity went up 100%.",
        technologies=["C#", "MVC", "SQL"],
        metrics=[Metric(value="2×", label="plant productivity")],
    ),
]

# attack, defense and effect only show once Dark Magician Girl buffs the page and every card becomes a duel monster
skills_data = [
    Skill(
        title="Leading Teams",
        icon="TbUserCode",
        description=(
            "My calendar is mostly 1:1s, and I like it that way. I'd rather unblock five engineers before lunch "
            "than write the clever thing myself."
        ),
        attack=2500,
        defense=2100,
        effect="Once per sprint: every engineer on your side of the field is unblocked.",
    ),
    Skill(
        title="AI & LLMs",
        icon="TbSparkles",
        description=(
            "Models get things wrong, so I treat them like any other dependency: guardrails, tests and a "
            "fallback. A boring right answer beats a brilliant wrong one."
        ),
        attack=2800,
        defense=1700,
        effect="When a model hallucinates, negate it and return a grounded answer instead.",
    ),
    Skill(
        title="Cloud & Infra",
        icon="FaAws",
        description=(
            "Functions when traffic spikes, containers when it doesn't, and nothing clicked together by hand in a "
            "console. If it isn't in code, it doesn't exist."
        ),
        attack=2300,
        defense=2800,
        effect="Cannot be destroyed by a Friday deploy.",
    ),
    Skill(
        title="Frontend & UX",
        icon="TbLayoutDashboard",
        description=(
            "Component libraries a whole product can share, and the small stuff people only notice when it's "
            "missing: loading states, dark mode, copy that sounds like a person."
        ),
        attack=2400,
        defense=2000,
        effect="Flip every loading spinner on the field into a skeleton.",
    ),
    Skill(
        title="Data & Search",
        icon="TbDatabase",
        description=(
            "I start from how the data will be read and work backwards. Documents when the access patterns are "
            "known, tables when the relationships matter, an index when people need answers fast."
        ),
        attack=2200,
        defense=2500,
        effect="Search your deck for any record and add it to your hand. Indexed, of course.",
    ),
    Skill(
        title="Quality & Security",
        icon="TbTestPipe",
        description=(
            "Unit tests for the logic, end to end tests for the paths people actually click, and a CI that's "
            "allowed to say no. Secrets and alerts go in before launch, not after the first 3 a.m. page."
        ),
        attack=1900,
        defense=3000,
        effect="Negate any attack that skipped CI.",
    ),
]

navbar_data = [
    NavBarItem(title="Home", url="/#home"),
    NavBarItem(title="About", url="/#about"),
    NavBarItem(title="Experience", url="/#work"),
    NavBarItem(title="Projects", url="/#projects"),
    NavBarItem(title="Skills", url="/#skills"),
    NavBarItem(title="Side quests", url="/#github"),
    NavBarItem(title="Education", url="/#education"),
    NavBarItem(title="Contact", url="/#contact"),
]

# the frontend splits the description on blank lines and renders the first paragraph as the lead
about_me_data = AboutMe(
    title="About",
    name="Cristopher Cervantes",
    headline="Engineering Manager & Tech Lead. Nine years of shipping software from a beach town in Baja to people all over the world.",
    summary=(
        "Engineering Manager and Tech Lead with 9+ years building production software. At PSL Group I grew from "
        "Senior Application Developer to running engineering for FirstWord, DGPL, MEC and AMI. Before that: "
        "payroll and attendance software for three countries, and factory software that doubled a plant's output."
    ),
    role="Tech Lead & Engineering Manager",
    years_of_experience=9,
    location="Rosarito, Mexico",
    timezone="Pacific Time",
    languages=[Language(name="Spanish"), Language(name="English")],
    main_stack=["TypeScript", "Next.js", "React", "Node.js", "AWS", "Serverless", "Bedrock", "LLMs"],
    editor="Neovim",
    expertise=[
        "Engineering management",
        "Technical leadership",
        "AI agents and LLM products",
        "Serverless architecture",
        "Design systems",
        "Infrastructure as code",
        "CI/CD and release pipelines",
    ],
    # self rated out of 5: the main stack first, then the other tools named in the work history
    skill_levels=[
        SkillLevel(name="TypeScript", level=5, category="Languages"),
        SkillLevel(name="Next.js", level=5, category="Frontend"),
        SkillLevel(name="React", level=5, category="Frontend"),
        SkillLevel(name="Node.js", level=5, category="Backend"),
        SkillLevel(name="AWS", level=5, category="Cloud & DevOps"),
        SkillLevel(name="Serverless", level=5, category="Cloud & DevOps"),
        SkillLevel(name="Bedrock", level=5, category="AI"),
        SkillLevel(name="LLMs", level=5, category="AI"),
        SkillLevel(name="C#", level=5, category="Languages"),
        SkillLevel(name="JavaScript", level=5, category="Languages"),
        SkillLevel(name="Lambda", level=5, category="Cloud & DevOps"),
        SkillLevel(name="DynamoDB", level=5, category="Data"),
        SkillLevel(name="Aurora", level=4, category="Data"),
        SkillLevel(name="OpenSearch", level=4, category="Data"),
        SkillLevel(name="Terraform", level=4, category="Cloud & DevOps"),
        SkillLevel(name="Kubernetes", level=4, category="Cloud & DevOps"),
        SkillLevel(name="GitHub Actions", level=4, category="Cloud & DevOps"),
        SkillLevel(name="Docker", level=4, category="Cloud & DevOps"),
        SkillLevel(name="PostgreSQL", level=4, category="Data"),
        SkillLevel(name="SQL", level=4, category="Data"),
        SkillLevel(name="MVC", level=4, category="Backend"),
        SkillLevel(name="PHP", level=4, category="Languages"),
        SkillLevel(name="Python", level=4, category="Languages"),
        SkillLevel(name="Azure", level=3, category="Cloud & DevOps"),
    ],
    education=[
        Education(
            school="Instituto Tecnológico de Tijuana",
            url="https://www.tijuana.tecnm.mx/",
            location="Tijuana, Mexico",
            degree="B.S. in Computer Systems Engineering",
            original_name="Ingeniería en Sistemas Computacionales",
            highlights=[
                "Algorithms, databases, networks and more late nights than I'd like to count. Most of what I still "
                "lean on started here.",
                "Part of TecNM, Mexico's national network of public engineering schools.",
            ],
        ),
    ],
    certifications=[
        Certification(
            name="AWS Certified Developer \u2013 Associate",
            issuer="Amazon Web Services",
            level="Associate",
            description=(
                "Building, deploying, securing and debugging applications on AWS services like Lambda, DynamoDB, "
                "API Gateway and IAM."
            ),
        ),
        Certification(
            name="AWS Certified Cloud Practitioner",
            issuer="Amazon Web Services",
            level="Foundational",
            description="The AWS Cloud from the ground up: core services, security, pricing and the shared responsibility model.",
        ),
    ],
    description=(
        "I'm 32 and I'm from Rosarito, Baja California, a beach town just south of Tijuana. My first production "
        "code ran at the border, and 9+ years later the things I build are used by people I'll never meet, in "
        "countries I've never been to.\n\n"
        "I didn't show up knowing much. I was an intern who could barely scratch out a few lines of code, and I "
        "got better one job at a time, until I was one of the people the team leaned on at every company I "
        "joined.\n\n"
        "These days I'm half Engineering Manager, half Tech Lead. I set the priorities, run the 1:1s and plan "
        "the roadmap, and I still open pull requests and leave long comments on other people's. When I push back "
        "on a design I bring another way to do it, because a no on its own doesn't teach anybody anything.\n\n"
        "Off the clock I'm working out, with my family, or every now and then a few volumes deep into a manga "
        "or a video game. A few of those games left relics hidden around this page. Good luck."
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
