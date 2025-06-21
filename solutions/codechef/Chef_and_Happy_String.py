string = "hrquryisigmzguoztohmkwpogrxtoyxbapwmptieqpalfaqypwsstxyziepchoaqfskeiqoznrlnrshfzqulntcblztzfzxjgwudrlmdpgsfvjbbceqlbbwtupkxlcvbjxroytqhurcndrkgsmpfahqyarnewnybqfmtbtisormirmqhcuectnsuopcuayrrmvuoxkhtwlgycyohddxyqsurmcwydbhjogtxhaceecrqcmiazumotnlzteodttxusjhonfjgwebahlstkkjajhmafqwbkcxlbxkzkwutjwiurfadwdbmmhduyjtqouhybgyxcmytyphpnjnvorqjvgpkpfmdeesrwtdrtjdmnyjgqfxahbiwalbezvmlfsdxasjmcqrunckwwxnldaokwhtnqxbfsyezffpkgedngibchhlccrobqvkfubhjuiyljwqffvxffyehuxhcqvkrrtqbvbqbarhkoxmkkpagrujbhclcrpuvkkxegudhhfjteycflodpyrakgtdgoxmfqlaiyoocmyfddysrkwdizuhcwtmzurskmdyphkhvrzhomcoaynqckdalzsepmitwowixptegzedcgmxiagmzgzpxsoawhewmdrysimpxfkmectifkuscxgrzcjjifabkkpmuaxzhkbfepmfmaudhmlfxcmccdbxqrzroyfwabfckdjernlxzwffnlxctxovdwmcdwssrgcssrvxxthfuqdxvqbfexrwxvmetiuxpjoqeedkrydysmzgtmglqytlyjfawpmkvsobvgepfauhjkmhevzqybifhdukzbtydswisgqzbcvwxssvweogctjydglwjtdhsffkgruqbttvkgptfbddlzmkafnlrtxlzqflizorkzghlvmnjqinlkodtruummlfxxvnzwsnjmskgxbwpdmirqbshneigitffrlfsdojtvdrgojznjyxogloebwhblnzrduyebvfrkfsf"
point = 0
length = len(string)
flag = False
while point <= length - 2:
    if (string[point] in ["a", "e", "i", "o", "u"]) and (
        string[point + 1] in ["a", "e", "i", "o", "u"]
    ):
        flag = True
    point += 1
if flag:
    print("Happy")
else:
    print("Sad")
