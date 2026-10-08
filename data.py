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
            "I joined as Tech Lead on FirstWord and now manage engineering for all four of our products in "
            "production. I set priorities, review architecture, mentor the engineers and keep releases on a "
            "regular schedule, and I still write a lot of the code. "
            "On the frontend, one React codebase runs three brands (FirstWord Pharma, HealthTech and Reports), "
            "and I built FirstWord Manager, the Next.js workspace the team uses for newsletters, news alerts, "
            "OpenSearch feeds, SSO clients and user access. "
            "Behind it sits a serverless API in TypeScript on Lambda, API Gateway and DynamoDB that also powers "
            "FirstWord AI: versioned agents that talk to Claude through Amazon Bedrock, with streaming "
            "responses, guardrails and a knowledge base. "
            "The older services are Symfony and PHP on MySQL and Aurora, plus the SSO and newsletter pipelines. "
            "Infrastructure is Terraform across our AWS accounts, apps run on EKS through ArgoCD, and every repo "
            "deploys with shared GitHub Actions workflows I maintain. I also set up the Claude Code tooling the "
            "whole team uses day to day."
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
            "MySQL",
            "OpenSearch",
            "Terraform",
            "Kubernetes",
            "GitHub Actions",
            "PHP",
            "Symfony",
            "Docker",
            "Jira",
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
        description="Built internal tools for Hisense México's corporate offices and factory floor.",
        detailed_description=(
            "I worked in C#, ASP.NET MVC and SQL on internal projects for the corporate office and the factory. I "
            "built the IT ticketing system from scratch, worked on the corporate website, and wrote tools that "
            "connected to internal systems so managers could follow manufacturing performance in real time."
        ),
        technologies=["C#", "MVC", "SQL"],
        image="hisense.png",
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
    ),
]

skills_data = [
    Skill(
        title="Engineering Management",
        icon="TbUserCode",
        description=(
            "I mentor engineers, set priorities and keep releases on schedule. When there's a tradeoff I explain "
            "it, and I want everyone on the team to know why we're building something the way we are."
        ),
    ),
    Skill(
        title="AI & LLMs",
        icon="TbSparkles",
        description=(
            "I build LLM features that ship to real users: agents on Amazon Bedrock with Claude, streaming "
            "responses, tool use, guardrails and knowledge bases. I also roll out AI coding tools so the whole "
            "team gets faster, not just me."
        ),
    ),
    Skill(
        title="AWS & Serverless",
        icon="FaAws",
        description=(
            "AWS certified, and I've used most of the platform: Lambda, API Gateway, Bedrock, S3, SQS, SNS, "
            "EventBridge, Step Functions, DynamoDB, Aurora, OpenSearch, CloudFront and Cognito. DynamoDB when the "
            "access patterns are known, a relational database when the data has real relationships."
        ),
    ),
    Skill(
        title="Languages & Frameworks",
        icon="SiNextdotjs",
        description=(
            "TypeScript, React, Next.js and Node.js day to day, plus PHP and Symfony on the older services. "
            "Before that, years of C# and ASP.NET MVC, with some Python and Go along the way."
        ),
    ),
    Skill(
        title="Frontend & UX",
        icon="TbLayoutDashboard",
        description=(
            "Design systems, component libraries and multi brand apps from a single codebase. I care about the "
            "small stuff too: loading states, dark mode, i18n and copy that sounds like a person wrote it."
        ),
    ),
    Skill(
        title="Data & Search",
        icon="TbDatabase",
        description=(
            "MySQL, Aurora, PostgreSQL and DynamoDB for storage, OpenSearch for feeds and full text search. I "
            "model the data around how it gets read, then make sure the indexes agree."
        ),
    ),
    Skill(
        title="Testing & Quality",
        icon="TbTestPipe",
        description=(
            "Jest and Vitest for units, Cypress and Playwright for the flows users actually click through, and "
            "CI that blocks the merge when coverage drops. Tests are how the next engineer trusts my code."
        ),
    ),
    Skill(
        title="Infrastructure & Delivery",
        icon="SiNeovim",
        description=(
            "Terraform for the infrastructure, Docker and Kubernetes with ArgoCD for running it, and shared GitHub "
            "Actions workflows so every repo deploys the same way. Neovim for writing all of it."
        ),
    ),
    Skill(
        title="Security & Observability",
        icon="GrShieldSecurity",
        description=(
            "I set up logging, error tracking and audit trails early so problems show up before users report "
            "them, and I keep auth, secrets and permissions locked down from the start."
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
    skill_levels=[
        SkillLevel(name="TypeScript", level=5),
        SkillLevel(name="Next.js", level=5),
        SkillLevel(name="React", level=5),
        SkillLevel(name="Node.js", level=5),
        SkillLevel(name="AWS", level=5),
        SkillLevel(name="Serverless", level=5),
        SkillLevel(name="Bedrock", level=5),
        SkillLevel(name="LLMs", level=5),
        SkillLevel(name="Lambda", level=5),
        SkillLevel(name="DynamoDB", level=5),
        SkillLevel(name="API Gateway", level=5),
        SkillLevel(name="JavaScript", level=5),
        SkillLevel(name="Aurora", level=4),
        SkillLevel(name="MySQL", level=4),
        SkillLevel(name="OpenSearch", level=4),
        SkillLevel(name="S3", level=4),
        SkillLevel(name="SQS", level=4),
        SkillLevel(name="SNS", level=4),
        SkillLevel(name="EventBridge", level=4),
        SkillLevel(name="Step Functions", level=4),
        SkillLevel(name="Terraform", level=4),
        SkillLevel(name="Docker", level=4),
        SkillLevel(name="Kubernetes", level=4),
        SkillLevel(name="ArgoCD", level=4),
        SkillLevel(name="GitHub Actions", level=4),
        SkillLevel(name="Jest", level=4),
        SkillLevel(name="PHP", level=4),
        SkillLevel(name="Symfony", level=4),
        SkillLevel(name="Jira", level=4),
        SkillLevel(name="Neovim", level=4),
        SkillLevel(name="C#", level=5),
        SkillLevel(name="MVC", level=4),
        SkillLevel(name="SQL", level=4),
        SkillLevel(name="PostgreSQL", level=4),
        SkillLevel(name="Python", level=4),
        SkillLevel(name="Go", level=3),
        SkillLevel(name="SAP", level=3),
        SkillLevel(name="Azure", level=3),
        SkillLevel(name="Photoshop", level=3),
        SkillLevel(name="Procreate", level=3),
    ],
    description=(
        "9+ years of building production software, from early prototypes to enterprise platforms used in "
        "three countries.\n\n"
        "I worked my way up from intern to Senior Developer, Tech Lead and Engineering Manager. Today I lead "
        "engineering across several products in production: setting priorities, unblocking people and shipping "
        "releases without surprises.\n\n"
        "I've worked every stage of the software lifecycle, from Terraform, Kubernetes and CI/CD pipelines, "
        "through APIs, databases and LLM integrations, all the way up to the React screens people actually "
        "click on. That's why I can still go deep with anyone on the team, wherever the problem lives. I like "
        "hard problems, and software the next engineer can pick up on their own."
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
