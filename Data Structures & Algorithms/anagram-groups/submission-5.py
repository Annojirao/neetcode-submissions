class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = dict()
        for i, elem in enumerate(strs):
            if "".join(sorted(elem)) in result_dict.keys():
                result_dict.get("".join(sorted(elem))).append(elem)
            else:
                result_dict["".join(sorted(elem))] = [elem]

        return list(result_dict.values())
