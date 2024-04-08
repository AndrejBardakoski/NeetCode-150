from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output = output + str(len(s)) + ":" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        index_ = s.find(":")
        while index_ != -1:
            l = int(s[:index_])
            subs = s[index_ + 1:index_ + 1 + l]
            output.append(subs)
            s = s[index_ + 1 + l:]
            index_ = s.find(":")
        return output
