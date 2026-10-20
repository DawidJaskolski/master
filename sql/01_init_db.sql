CREATE TABLE IF NOT EXISTS evaluation_runs (
    run_id VARCHAR(64) PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    workflow_id VARCHAR(10) NOT NULL,
    system_name VARCHAR(50) NOT NULL,
    architecture VARCHAR(30) NOT NULL,
    model_name VARCHAR(50) NOT NULL,
    prompt_tokens INT NOT NULL,
    completion_tokens INT NOT NULL,
    total_cost_usd NUMERIC(8, 5) NOT NULL,
    latency_seconds NUMERIC(6, 2) NOT NULL,
    workflow_step_recall NUMERIC(5, 2) NOT NULL,
    warning_extraction_recall NUMERIC(5, 2) NOT NULL,
    hallucination_score INT NOT NULL,
    generated_doc_markdown TEXT NOT NULL,
    judge_feedback TEXT
);