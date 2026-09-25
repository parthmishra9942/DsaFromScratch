class Solution:
    def braceExpansionII(self, expression):
        def parse_expr(i):
            # Handles comma-separated expressions
            result = set()

            current, i = parse_concat(i)
            result |= current

            while i < len(expression) and expression[i] == ',':
                i += 1
                current, i = parse_concat(i)
                result |= current

            return result, i

        def parse_concat(i):
            # Handles adjacent expressions
            result = {""}

            while i < len(expression) and expression[i] not in "},":
                if expression[i] == '{':
                    part, i = parse_expr(i + 1)
                    i += 1       # skip '}'
                else:
                    part = {expression[i]}
                    i += 1

                result = {
                    a + b
                    for a in result
                    for b in part
                }

            return result, i

        result, _ = parse_expr(0)
        return sorted(result)