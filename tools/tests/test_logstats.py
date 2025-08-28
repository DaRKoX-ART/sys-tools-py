from tools.logstats import logstats
from pathlib import Path

def test_counts(tmp_path: Path):
    sample = tmp_path/"sample.log"
    sample.write_text("INFO hi\nERROR boom\nDEBUG x\nWARN y\n")
    assert logstats(sample) == {"INFO":1,"ERROR":1,"DEBUG":1,"WARN":1}
