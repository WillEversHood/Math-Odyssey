from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class GenFormalizer():
    """GenFormalizer crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    '''
    Additional Attributes of the Agent Class:
    agent_executor: An instance of the CrewAgentExecutor class.
    role: The role of the agent.
    goal: The objective of the agent.
    backstory: The backstory of the agent.
    knowledge: The knowledge base of the agent.
    config: Dict representation of agent configuration.
    llm: The language model that will run the agent.
    function_calling_llm: The language model that will handle the tool calling for this agent, it overrides the crew function_calling_llm.
    max_iter: Maximum number of iterations for an agent to execute a task.
    max_rpm: Maximum number of requests per minute for the agent execution to be respected.
    verbose: Whether the agent execution should be in verbose mode.
    allow_delegation: Whether the agent is allowed to delegate tasks to other agents.
    tools: Tools at agents disposal
    step_callback: Callback to be executed after each step of the agent execution.
    knowledge_sources: Knowledge sources for the agent.
    embedder: Embedder configuration for the agent.
    '''
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            temperature=0.0,  
            llm=LLM(model='gemini/gemini-2.5-flash', max_tokens=100000) 
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'], # type: ignore[index]
            verbose=True,
            temp=0
        )
    @agent
    def evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    ''' Additional Attributes:
        agent: Agent responsible for task execution. Represents entity performing task.
        async_execution: Boolean flag indicating asynchronous task execution.
        callback: Function/object executed post task completion for additional actions.
        config: Dictionary containing task-specific configuration parameters.
        context: List of Task instances providing task context or input data.
        description: Descriptive text detailing task's purpose and execution.
        expected_output: Clear definition of expected task outcome.
        output_file: File path for storing task output.
        create_directory: Whether to create the directory for output_file if it doesn't exist.
        output_json: Pydantic model for structuring JSON output.
        output_pydantic: Pydantic model for task output.
        security_config: Security configuration including fingerprinting.
        tools: List of tools/resources limited for task execution.
        allow_crewai_trigger_context: Optional flag to control crewai_trigger_payload injection.
                              None (default): Auto-inject for first task only.
                              True: Always inject trigger payload for this task.
                              False: Never inject trigger payload, even for first task.
    '''
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the GenFormalizer crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
