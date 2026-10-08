from models import Project, Skill, SkillLevel, NavBarItem, AboutMe, ContactInfo, SocialLink

# Data for the portfolio projects and skills
projects_data = [
    Project(
        title="PSL Group / FirstWord",
        url="https://www.pslgroup.com/",
        description=(
            "I manage engineering for all of PSL Group's products in production, including FirstWord, a pharma and "
            "medical news platform: web apps, newsletters, content feeds and AI models."
        ),
        detailed_description=(
            "I joined as Tech Lead on FirstWord and now manage engineering for all four of our products in "
            "production. Each one has its own stack, from PHP and Python services to Node.js, React and Next.js "
            "apps, all running on AWS. I set priorities across the four, review architecture, mentor the engineers "
            "and make sure each product ships on a regular schedule. Most of the newer work is TypeScript on "
            "Lambda and other serverless AWS services, with DynamoDB, Aurora and MySQL for data. Deploys run "
            "through GitHub Actions and the work lives in Jira. "
            "Users browse apps, read newsletters and request deeper analysis, some of it backed by a custom AI "
            "model. I still write code and jump in on the hard bugs when the team needs it."
        ),
        technologies=[
            "TypeScript",
            "Next.js",
            "Serverless",
            "AWS",
            "Lambda",
            "DynamoDB",
            "Aurora",
            "MySQL",
            "React",
            "Node.js",
            "GitHub Actions",
            "Jira",
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
        title="AWS & Serverless",
        icon="FaAws",
        description=(
            "AWS certified, and I've used most of the platform: Lambda, API Gateway, S3, SQS, SNS, EventBridge, "
            "Step Functions, DynamoDB, Aurora, CloudFront, CloudWatch, Cognito, IAM and CloudFormation."
        ),
    ),
    Skill(
        title="Languages & Frameworks",
        icon="SiNextdotjs",
        description=(
            "TypeScript, JavaScript, React and Next.js day to day. Before that, years of C# and ASP.NET MVC, "
            "plus PHP, Python and Go."
        ),
    ),
    Skill(
        title="Databases",
        icon="SiAmazondynamodb",
        description=(
            "MySQL, SQL Server, PostgreSQL, Aurora and DynamoDB. I design DynamoDB tables around how the data is "
            "read, and use a relational database when the data has real relationships. I've also worked with SAP."
        ),
    ),
    Skill(
        title="Tooling & Delivery",
        icon="SiNeovim",
        description=(
            "Neovim for writing code, GitHub Actions for CI/CD, Docker and Kubernetes for running it, Jira for "
            "tracking the work. Photoshop and Procreate when a project needs design work."
        ),
    ),
    Skill(
        title="Security & Observability",
        icon="GrShieldSecurity",
        description=(
            "I set up logging, error tracking and analytics early so problems show up before users report them, "
            "and I keep auth, secrets and permissions locked down from the start."
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
    main_stack=["TypeScript", "Next.js", "Serverless", "AWS", "Lambda", "DynamoDB", "Aurora", "MySQL"],
    editor="Neovim",
    # self rated out of 5, listed by relevance: main stack, then today's tooling, then earlier stacks
    skill_levels=[
        SkillLevel(name="TypeScript", level=4),
        SkillLevel(name="Next.js", level=4),
        SkillLevel(name="Serverless", level=4),
        SkillLevel(name="AWS", level=4),
        SkillLevel(name="Lambda", level=4),
        SkillLevel(name="DynamoDB", level=4),
        SkillLevel(name="Aurora", level=4),
        SkillLevel(name="MySQL", level=4),
        SkillLevel(name="Node.js", level=5),
        SkillLevel(name="React", level=4),
        SkillLevel(name="JavaScript", level=4),
        SkillLevel(name="API Gateway", level=4),
        SkillLevel(name="S3", level=4),
        SkillLevel(name="SQS", level=4),
        SkillLevel(name="SNS", level=4),
        SkillLevel(name="EventBridge", level=4),
        SkillLevel(name="GitHub Actions", level=4),
        SkillLevel(name="Jira", level=4),
        SkillLevel(name="Docker", level=4),
        SkillLevel(name="Kubernetes", level=4),
        SkillLevel(name="Neovim", level=4),
        SkillLevel(name="C#", level=5),
        SkillLevel(name="MVC", level=4),
        SkillLevel(name="SQL", level=4),
        SkillLevel(name="PostgreSQL", level=4),
        SkillLevel(name="Python", level=4),
        SkillLevel(name="PHP", level=4),
        SkillLevel(name="Go", level=3),
        SkillLevel(name="SAP", level=3),
        SkillLevel(name="Azure", level=3),
        SkillLevel(name="Photoshop", level=3),
        SkillLevel(name="Procreate", level=3),
    ],
    description=(
        "I'm Cristopher Cervantes, a Tech Lead and Engineering Manager with 9+ years of experience building "
        "production software, from early prototypes to enterprise platforms used in three countries.\n\n"
        "I worked my way up from intern to Senior Developer, Tech Lead and Engineering Manager. Today I lead "
        "engineering across several products in production: setting priorities, unblocking people and shipping "
        "releases without surprises.\n\n"
        "I've built across frontend, backend, cloud and data, so I can still go deep with anyone on the team. I "
        "like hard problems, and software the next engineer can pick up on their own."
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
