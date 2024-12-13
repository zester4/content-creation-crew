from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool

@CrewBase
class ContentCreationCrew:
    """Content Creation Crew for Dynamic Content Generation"""

    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'],
            verbose=True,
            tools=[
                SerperDevTool(),
                WebsiteSearchTool()
            ]
        )

    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_strategist'],
            verbose=True
        )

    @agent
    def content_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer'],
            verbose=True
        )

    @agent
    def seo_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_optimizer'],
            verbose=True,
            tools=[WebsiteSearchTool()]
        )

    @task
    def trend_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['trend_research_task'],
            output_file='output/trend_research.md'
        )

    @task
    def content_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_strategy_task'],
            output_file='output/content_strategy.md'
        )

    @task
    def content_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_creation_task'],
            output_file='output/content_draft.md'
        )

    @task
    def seo_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_optimization_task'],
            output_file='output/optimized_content.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Content Creation Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
