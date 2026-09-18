import re
import time


class HybridPromptDetector:

    def __init__(self):

        # Stage 1: Rule-based detection
        self.heuristic_patterns = [
            (
                r"(?i)ignore\s+(all\s+)?previous\s+instructions",
                "Instruction Override"
            ),
            (
                r"(?i)system\s+prompt",
                "System Prompt Extraction"
            ),
            (
                r"(?i)you\s+are\s+now\s+in\s+developer\s+mode",
                "Developer Mode Manipulation"
            ),
            (
                r"(?i)bypass\s+security",
                "Security Bypass"
            ),
            (
                r"(?i)override\s+rules",
                "Rule Override"
            )
        ]

        # Stage 2: Suspicious keyword detection
        self.suspicious_keywords = {
            "jailbreak": "Jailbreak Attempt",
            "dan": "DAN Mode Attempt",
            "unrestricted": "Unrestricted Mode Request",
            "root access": "Unauthorized Access Request"
        }

    # Stage 1: Rule-based detection
    def stage_1_heuristics(self, prompt: str):

        for pattern, attack_type in self.heuristic_patterns:

            if re.search(pattern, prompt):

                return {
                    "detected": True,
                    "attack_type": attack_type,
                    "reason": f"Detected pattern related to {attack_type.lower()}."
                }

        return {
            "detected": False
        }

    # Stage 2: Keyword detection
    def stage_2_keyword_analysis(self, prompt: str):

        prompt_lower = prompt.lower()

        for keyword, attack_type in self.suspicious_keywords.items():

            if keyword in prompt_lower:

                return {
                    "detected": True,
                    "attack_type": attack_type,
                    "reason": f"Suspicious keyword detected: '{keyword}'."
                }

        return {
            "detected": False
        }

    # Main scanning function
    def scan(self, prompt: str):

        start_time = time.perf_counter()

        # Handle empty input
        if not prompt.strip():

            return {
                "status": "INVALID",
                "risk_level": "NONE",
                "attack_type": "None",
                "reason": "Prompt cannot be empty.",
                "latency_ms": 0
            }

        # Stage 1 check
        stage_1_result = self.stage_1_heuristics(prompt)

        if stage_1_result["detected"]:

            latency = (time.perf_counter() - start_time) * 1000

            return {
                "status": "BLOCKED",
                "risk_level": "HIGH",
                "attack_type": stage_1_result["attack_type"],
                "reason": stage_1_result["reason"],
                "stage": "Stage 1: Heuristics",
                "latency_ms": round(latency, 2)
            }

        # Stage 2 check
        stage_2_result = self.stage_2_keyword_analysis(prompt)

        if stage_2_result["detected"]:

            latency = (time.perf_counter() - start_time) * 1000

            return {
                "status": "SUSPICIOUS",
                "risk_level": "MEDIUM",
                "attack_type": stage_2_result["attack_type"],
                "reason": stage_2_result["reason"],
                "stage": "Stage 2: Keyword Analysis",
                "latency_ms": round(latency, 2)
            }

        # Safe prompt
        latency = (time.perf_counter() - start_time) * 1000

        return {
            "status": "SAFE",
            "risk_level": "LOW",
            "attack_type": "None",
            "reason": "No known suspicious patterns detected.",
            "stage": "Cleared",
            "latency_ms": round(latency, 2)
        }


# Program execution
if __name__ == "__main__":

    detector = HybridPromptDetector()

    print("\n--- PromptGuard: Prompt Injection Detector ---")
    print("Type 'exit' to stop the program.\n")

    while True:

        prompt = input("Enter your prompt: ")

        if prompt.lower() == "exit":
            print("\nProgram closed.")
            break

        result = detector.scan(prompt)

        print("\n--- Detection Result ---")

        for key, value in result.items():
            print(f"{key}: {value}")

        print("-" * 40)