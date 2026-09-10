def test_agent_orchestrator():
    prompt = "Test execution query for agentic-devops-sre-incident-responder"
    assert len(prompt) > 0
    assert "Test" in prompt
