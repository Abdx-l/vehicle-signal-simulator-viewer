from publisher import signal
def test_range():
 for t in range(10000):
  s=signal(t);assert 0<=s["speed"]<=85;assert 0<=s["soc"]<=100;assert 19<=s["temperature"]<=23
