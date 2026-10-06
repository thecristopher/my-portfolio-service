from models import Project, Skill, SkillLevel, NavBarItem, AboutMe, ContactInfo, SocialLink

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group / FirstWord",
        url="https://www.pslgroup.com/",
        description=(
            "Leading engineering for FirstWord: a serverless TypeScript platform on AWS that delivers pharma and "
            "medical insights through web apps, newsletters, content feeds and AI models."
        ),
        detailed_description=(
            "I was FirstWord's Tech Lead and now manage its engineering team. I own the technical direction and the "
            "delivery: setting priorities, reviewing architecture, growing the engineers on the team and keeping a "
            "steady release rhythm. The platform runs on TypeScript and Next.js, with serverless services on AWS backed "
            "by DynamoDB and MySQL. It lets users browse applications, read newsletters and request deeper insights, "
            "all enhanced by a custom AI model, and my AWS certifications still earn their keep whenever the team "
            "needs a second pair of eyes on a tricky problem."
        ),
        technologies=[
            "TypeScript",
            "Next.js",
            "Serverless",
            "AWS",
            "DynamoDB",
            "MySQL",
            "React",
            "Node.js",
            "Python",
            "PHP",
            "Docker",
            "PostgreSQL",
        ],
        image="psl.png",
    ),
    Project(
        title="Grupo Tress",
        url="https://www.tress.com.mx/",
        description=(
            "Built enterprise payroll software and the component library behind a cloud payroll platform "
            "serving Mexico, the U.S. and Canada."
        ),
        detailed_description=(
            "As a Senior Developer, I maintained and expanded core applications with React, C#, Node.js, SQL and "
            "PostgreSQL across AWS, Azure and Docker. I led development of a payroll app where employees enroll "
            "themselves and manage their own attendance. I also designed GTI Controls, a reusable UI component "
            "library that powers Interis Works, a cloud payroll system built on microservices and React. Together "
            "with Sistema Tress, it stands as a pioneer in payroll software across Mexico, the U.S. and Canada."
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
        description="Built internal platforms that raised productivity across corporate offices and the factory floor.",
        detailed_description=(
            "Using C#, ASP.NET MVC and SQL, I led several projects to boost productivity across Hisense México's "
            "corporate and manufacturing operations. That included an IT ticketing system built from scratch and "
            "contributions to the official corporate website. The tools plugged into internal systems to streamline "
            "manufacturing performance and surface improvements as they happened."
        ),
        technologies=["C#", "MVC", "SQL"],
        image="hisense.png",
    ),
    Project(
        title="Umbrella Seguros",
        url="https://www.umbrella-seguros.com/",
        description="Modernized an insurance management platform for speed, usability and digital reach.",
        detailed_description=(
            "I modernized Umbrella's insurance management platform with C#, MVC, SQL, Python and JavaScript. "
            "Beyond reworking the school insurance workflows, I maintained and extended core features, sharpening "
            "the UX and the operational logic so the platform could scale with its users."
        ),
        technologies=["C#", "MVC", "SQL", "Python", "JavaScript"],
        image="umbrella.jpg",
    ),
    Project(
        title="Systems Communications",
        url="https://www.systemscomm.net/es/inicio/",
        description="Where it started: logistics software for the Tijuana customs office, built during my internship.",
        detailed_description=(
            "During my internship I built a transportation inventory system used by the Tijuana customs office, "
            "tracking trucks as they entered and left in a busy, real operation. Working in PHP, C# and SQL, this is "
            "where clean code stopped being a theory and became a habit."
        ),
        technologies=["PHP", "C#", "SQL"],
        image="syscoms.png",
    ),
]

skills_data = [
    Skill(
        title="Engineering Management",
        icon="TbUserCode",
        description=(
            "I grow engineers, set clear priorities and keep delivery predictable. Honest tradeoffs, healthy "
            "teams, and everyone knowing why we're building it this way."
        ),
    ),
    Skill(
        title="Serverless on AWS",
        icon="FaAws",
        description=(
            "AWS certified and serverless by default: functions, queues and managed services that scale with "
            "demand and stay cheap when it's quiet."
        ),
    ),
    Skill(
        title="TypeScript & Next.js",
        icon="SiNextdotjs",
        description=(
            "Typed end to end, from Next.js frontends to Node services, so refactors stay boring and bugs get "
            "caught long before they reach review."
        ),
    ),
    Skill(
        title="Data Modeling",
        icon="SiAmazondynamodb",
        description=(
            "DynamoDB designed around real access patterns, and MySQL where relationships matter. The data model "
            "is the architecture, so I treat it that way."
        ),
    ),
    Skill(
        title="Developer Experience",
        icon="SiNeovim",
        description=(
            "I live in Neovim and care about the tools around the team: fast feedback loops, calm CI and code "
            "reviews that actually teach something."
        ),
    ),
    Skill(
        title="Security & Observability",
        icon="GrShieldSecurity",
        description=(
            "Performance and trust go together. Analytics, error tracking and sensible security patterns, so "
            "problems surface early and the system tells you what's wrong."
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
    role="Engineering Manager",
    main_stack=["TypeScript", "Next.js", "Serverless", "AWS", "DynamoDB", "MySQL"],
    editor="Neovim",
    # self rated out of 5, listed by relevance: main stack, then today's tooling, then earlier stacks
    skill_levels=[
        SkillLevel(name="TypeScript", level=4),
        SkillLevel(name="Next.js", level=4),
        SkillLevel(name="Serverless", level=4),
        SkillLevel(name="AWS", level=4),
        SkillLevel(name="DynamoDB", level=4),
        SkillLevel(name="MySQL", level=4),
        SkillLevel(name="Node.js", level=5),
        SkillLevel(name="React", level=4),
        SkillLevel(name="Jira", level=4),
        SkillLevel(name="Docker", level=4),
        SkillLevel(name="Kubernetes", level=4),
        SkillLevel(name="Neovim", level=4),
        SkillLevel(name="C#", level=5),
        SkillLevel(name="Python", level=4),
        SkillLevel(name="PHP", level=4),
        SkillLevel(name="PostgreSQL", level=4),
        SkillLevel(name="SQL", level=4),
        SkillLevel(name="JavaScript", level=4),
        SkillLevel(name="MVC", level=4),
        SkillLevel(name="Azure", level=3),
    ],
    description=(
        "I'm Cristopher Cervantes, an engineering manager with 9+ years of shipping production software, from "
        "quick prototypes to enterprise platforms used across three countries.\n\n"
        "At PSL Group I lead engineering for FirstWord. I was its Tech Lead and now manage the team behind it: "
        "setting direction, growing engineers and keeping delivery steady on a serverless TypeScript platform "
        "built on AWS.\n\n"
        "Day to day that means TypeScript and Next.js up front, serverless services on AWS underneath, and DynamoDB "
        "and MySQL holding the data. Before that I worked across C# and .NET, PHP and Python, which is why I can "
        "still get into the details with any engineer on the team.\n\n"
        "I'm AWS certified as both a Cloud Practitioner and a Developer Associate, so infrastructure is part of "
        "the design conversation from day one, not an afterthought before launch.\n\n"
        "I write code in Neovim, review it with care, and believe the best teams ship with clear priorities, honest "
        "tradeoffs and code a teammate can pick up without a tour guide. I still love the kind of problem that makes "
        "other developers sigh dramatically."
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
            id=3, name="Instagram", url="https://www.instagram.com/thecristopher/"
        ),
    ],
)
