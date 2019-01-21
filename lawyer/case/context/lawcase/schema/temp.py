# coding=utf-8
import json
from util import decrypt_id_array

json_text = """[{\"RunEval\":\"w61Zw43CjsKCMBB+FsKMwoc2bHwBw6LDiUfDmMOjwqQhBl3DpcKgbCp7MsK+wrvDgMK6LMOQKsK4wrRYwpYvIWNow6fDr8O7ZsOaw5I4w5/Dh8Kbw60pwpLDsWfCunxPZXzDnC0+ZHJYw63Dl3LClWzCtsOMw7d8EhBOwos3wpAAMcKNDsO5D0AmwrJcwrErwqHCthDDoB3DjELCoHpgDMOFBSfDgA/DgCABw4TCgAnCoAY7w6AJw6AACRXCgEAjOCV4EMKEw4tZwpQcT8Kpw7zCisOSRMOOwoLCkELCkT3CjMO5w6dLwq5WPsOnC8Knb0vDisKEED7Ds8KKCU51wp/DuUTDu0zDsTrDv8O9T8KaWD7CnGnCkMKXw4/CkMKgw6zCpxHCsMKuw67DnQzDrgdrw6TCrcOVfcKYU8OVwpt+wrwMVWTCrVLCpMKkwqDDhcOww4B3wplkN0Yrwq/CrWl3w5R4RsOtacOdwr8Zw7TCsMOqa2rDhMK+dcKdGHDDn2zCnMKWTjUVUV17w5pkwrrDqsKMwoTDpzp0awwbL8KTecO8wrbCqsO4ChA2w5NWeBoTwpZyw63DvhzDk8ODwrTCv8OVBhvCoMOcA8K2w5XDncOyOHDDsBkJNmgmdiPCusK9wqvCj8Olw4xxMsOsLcK2w7IRw5bDpcOKw6EQN8Kae8KFw7pdWcObccO0wqNVwofDlMOjZsO0csOKwqbCmsKFw6DCjAdX\",\"Count\":\"115\"},{\"裁判要旨段原文\":\"本院认为，本案中双方当事人对位于跳磴镇双河村五社的三道拐水库及其周边共计28亩土地的所有权归双河村五社并无争议，同时，重庆市大渡口区人民政府大渡口府地决（2016）1号土地权属争议案件决定书决定：跳磴镇双河村三道拐水库占地28亩土地所有权归双河村五社所有。故双\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-12-20\",\"案件名称\":\"重庆市大渡口区跳蹬镇双河村五社与重庆市大渡口区跳蹬镇双河村村民委员会占有物返还纠纷二审民事判决书\",\"文书ID\":\"DcOOwqcBw4BADMOAw4DClVzDng3CusOuP1JCdUTDjT7DhwHCs8KSwpbChsKBXsKDCMOxSmXDisKNLVXDgmrDjHDDmMKhBsOawq/DgGXCvTN/wph+QU1seMKxwo3CrQ/Cl0vDhnvDkgDChQ8Qw7ZpM8Oewo7DrEvCkxLDosKEw4zDrVx5eU7CmzrCuWzDlsKmeMOjIcKSTcKkXcKpwrTDt8OuSBLDiMODwrdPwofChkMqw7rDvsKpwoHDlcOuN37CrMOxVwJXbMKxV8OnHw==\",\"审判程序\":\"二审\",\"案号\":\"（2017）渝05民终7697号\",\"法院名称\":\"重庆市第五中级人民法院\"},{\"裁判要旨段原文\":\"本院认为，当事人协商一致，可以解除合同。本案原、被告依法签订《汽车挂靠经营合同》，现原告因被告违约主张解除，被告亦同意，本院依法予以支持。\u0026#xA;综上，依据《中华人民共和国合同法》第八条、第六十条、第九十三条、《中华人民共和国民事诉讼法》第三十九条、第一百三\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-12-14\",\"案件名称\":\"重庆尊远物流有限公司与黄青松挂靠经营合同纠纷一审民事判决书\",\"文书ID\":\"FcKOwrkRBDEMw4NawpJkWk/CqMOPw73Cl3R7EQNwMHgcHMOuw6FyY8OJCQt7woHCqcKbGXZSwqdtDCHCrC/CpwvDqsOmw4saSsKAH8KTw7zCvhovwqVJwrcOGhTDh1HCr8Ogw5TDnDJxABvDtMKtRcKdLsOaFMKnbB3CqTBbLXnDpDHDlsKnw4bCiTfCgB0+wqJ+woLDhsOkcxTCkiRnwppjwp3CvwJsXi3Cn8ObwrdLw65jw782w5/Cl8KHw7jCo8O5XG1WPw==\",\"审判程序\":\"一审\",\"案号\":\"（2017）渝0104民初4828号\",\"法院名称\":\"重庆市大渡口区人民法院\"},{\"裁判要旨段原文\":\"本院认为，依法成立的合同受法律保护，双方当事人应当按照合同约定全面履行各自的义务。本案中，原、被告依法签订《汽车挂靠经营合同》，该合同系双方真实意思表示，合法有效，原、被告双方均应按照合同约定全面履行各自的义务。因被告对“是否履行合同约定的缴费义务”这一事实负\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-12-14\",\"案件名称\":\"重庆尊远物流有限公司与张国强挂靠经营合同纠纷一审民事判决书\",\"文书ID\":\"FcKOwrcBA0EMw4NWOmXCqVTDnH8kwr8bFigAbsKXMXBJUnvCl8OoFMOKUcOBw6LCtcKLXQl0InHCtsOJVcOYw4HCpMOxGCjCjsOLG1cxw4Zvw47CicKrw4bDucOuQlcfw4kxw63CvgEcVUHDtMKFw64OwpJHw5XCi8O7w7DCrMKUJsO4I8KudU0+BQDCrcKgwpPDj0LCg3DDgcOhcyopwqDDmXsiFGTDpMKbLQsswqXCm8OnF8OzdcOTA8O/D1HDkyDDrcKofw==\",\"审判程序\":\"一审\",\"案号\":\"（2017）渝0104民初4827号\",\"法院名称\":\"重庆市大渡口区人民法院\"},{\"裁判要旨段原文\":\"本院认为，依法成立的合同关系受法律保护，当事人应当按照合同约定全面履行自己的义务。本案中，原被告签订的《汽车挂靠经营合同》系当事人真实意思表示，合法有效，双方均应按照合同约定履行，被告何双银对其是否按照合同约定的期限支付管理服务费、保险费具有举证证明责任，但其\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-12-13\",\"案件名称\":\"重庆天浩物流有限公司与何双银挂靠经营合同纠纷一审民事判决书\",\"文书ID\":\"FcONwrkBA0EIw4DDgMKWw7hhQ8Oew75Lw7I5wpTCksOZw5TDiS3Cq8OpwpPDssKFwoXDjH4wEMObXhbDujhDwrEaI8OaLcOwwpwqw5daw5dHwox4wocdw5/DgsKNFcKwf2XDuzDDnFlLIEAaw6LDvGnCoyPCsCwzw5bChUrClsO9wrU9eMKpJsKdLsOyGcK1w7IZw71owr5FIsKaHG/DjsOdwpHCghnDiGLCqwgMS8OjcGjCngwmAcKewqkrCmTCtXNfwpBuw7gP\",\"审判程序\":\"一审\",\"案号\":\"（2017）渝0104民初3870号\",\"法院名称\":\"重庆市大渡口区人民法院\"},{\"裁判要旨段原文\":\"本院认为，被告人叶向前以非法牟利为目的，明知他人非法经营假冒伪劣烟草制品，仍然接受他人的委托，帮助他人雇佣货车运输假冒伪劣烟草制品，情节特别严重，其行为侵犯了国家对烟草制品专卖的正常管理秩序，已构成非法经营罪。公诉机关指控的事实和罪名成立，量刑建议适当，本院予\",\"不公开理由\":\"\",\"案件类型\":\"1\",\"裁判日期\":\"2017-11-27\",\"案件名称\":\"叶向前非法经营一审刑事判决书\",\"文书ID\":\"DcOLwrkBw4AwCATCsMKVw4DDvMKlMcOHw74jJcOqwqXCtcOJYsOFw5HCscK3X3LDmMOdPBHCtMKgw7Y4dUXCni/Cl8Kcw41Uw5bDrcOUeSzCvDNRPjHDrVAlEcOawqgub8KiesO/wpFRLcODPsKkYsO0XMOgPjnDhwHClRDDiMK6RTjDpzHCgFMTdF8pw6xSUsONI3vCisOQworCksKJaCxQNsKUw4YOwosjwovDmMOKO8KjU8OWwqxeTjvDlcKkwrEHCcOlw6oP\",\"审判程序\":\"一审\",\"案号\":\"（2017）渝0106刑初1457号\",\"法院名称\":\"重庆市沙坪坝区人民法院\"},{\"裁判要旨段原文\":\"本院经审查认为：被申请人谢华确实没有建设施工资质的自然人，双方签订的《厂房修建协议》无效。但是，根据最高人民法院《关于审理建设工程施工合同纠纷案件适用法律问题的解释》第二条，建设工程施工合同无效，但建设工程经竣工验收合格，承包人请求参照合同约定支付工程价款的，\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-11-14\",\"案件名称\":\"戴如桂与重庆市渝北区欧兴食品厂薛婧娇等建设工程施工合同纠纷申诉、申请再审民事裁定书\",\"文书ID\":\"DcOMwrcRw4BACADCsMKVw4jCocKEB8O2H8OJw651worDsMOrbmcAKHckwqHCiTfCjghMJ8K+aWPDm2bClsKYYcOMwqJSU8OALmt0VjgOZ8OYw7zDqFlew6tjHcKWGMKBw58Ww6XDo8O1VjXCjQ3DoS3Cl8ORw4zDsBZtwrXDh8Kxw5XDnMKbwroAfmdUPFZ6w7XCkC7CpsKewo7Drl/Cum7CrsK9LsOcBMOhwohcwrLDlUDDvVMZKMOuS8Kswo7Cv8KMKMOeIWrDvQA=\",\"审判程序\":\"再审审查与审判监督\",\"案号\":\"（2017）渝0112民申26号\",\"法院名称\":\"重庆市渝北区人民法院\"},{\"裁判要旨段原文\":\"本院认为，原、被告之间的《汽车挂靠经营合同》合法有效，双方均应当根据合同约定履行各自的权利义务，无证据显示被告已经按时缴纳保险费等，原告要求根据合同约定解除合同，符合双方约定及法律规定，本院依法予以支持。\u0026#xA;综上，本院依照《中华人民共和国合同法》第九十三\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-11-08\",\"案件名称\":\"重庆尊渝物流有限公司与秦兴有挂靠经营合同纠纷一审民事判决书\",\"文书ID\":\"DcOPw4kNADEIBMOBwpTCuMKMw43Ck8Ohw4g/wqTDnX/Cq8Kkw45Bw59nI8OlajjCrcObw5LCkSfClsO4IQXCgRxeAWjDnT3DoD1MUcOUIcKzb243P8KTW2wkARXDmT8owqULVlIOVFk9w7bCoMORw5TCuMOOdVYBwrfCu8OGw7TCq8KDwrzDt8K6BUzCjMOPw7ZvT8KFHMOgRMOseTPCjE7CkcKUw6ppHmjDqStLw5RxTsKHwpxywqLDqMOtw5LDoj5hwprDv1PCnMO2w7oA\",\"审判程序\":\"一审\",\"案号\":\"（2017）渝0104民初3869号\",\"法院名称\":\"重庆市大渡口区人民法院\"},{\"裁判要旨段原文\":\"本院认为，原、被告签订的《汽车挂靠经营合同》系双方真实意思表示，且不违反法律、行政法规的禁止性规定，依法成立并有效。双方均应按照合同约定履行合同。当事人可以约定一方解除合同的条件，解除条件成就时，解除权人可以解除合同。本案原、被告签订的《汽车挂靠经营合同》中约\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-10-10\",\"案件名称\":\"重庆大渡口汽车运输公司与徐先维挂靠经营合同纠纷一审民事判决书\",\"文书ID\":\"DcOLwrcRw4BACADCsMKVw4jCocOkCcO7wo9kw5c6wp3Ck8K3w7bCuUXCsMOgXsOAwopeZMOvWCtTRgHCpmbDncKgw6AzX3kCfMKJM2lWwrTCmQPDuyrCrcOQUHvDrm3DocKCwoRow6svw5pSGQLCtC/Cl3jCvQ3Ch35oDcO2XcOFwrfCoFzCo8OkMMKkHSbDjSAlN8O7w6jDrMKawqTCpsOOw7LCuMOVw6BgwqExwpJuwp/DvMKLwrdlw6ZgMMKEHMOLWcKIw4AFRMOgAw==\",\"审判程序\":\"一审\",\"案号\":\"（2017）渝0104民初1269号\",\"法院名称\":\"重庆市大渡口区人民法院\"},{\"裁判要旨段原文\":\"本院认为，上诉人张强自愿撤回上诉的申请符合法律规定，应予准许。依照《中华人民共和国民事诉讼法》第一百七十三条之规定，裁定如下\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-09-29\",\"案件名称\":\"张强与重庆智能水表集团有限公司劳动争议二审民事裁定书\",\"文书ID\":\"FcOOw4kRBDEIBEHClxrDhMO5RCDDvDdpZ8O/FRnCpXHDgsKoO8OfwqLDizV2w6M6QcKVO27DjjnDnsOnJGfDusOgw4QAUsOWwrh6wqXCsV/CgsOZw57CgcKsUcKow7rDnmfDjBR3eFXDl8K3QcOyBMKUVsOIwqF0w63CjWTDjl7DhGVgw6N5wrnCjcOmwrDCm1UEwqnCm35PUBLCscKQw4zCq8O9w74SRMKGQC/DuRA1WcOJRxHCncOnWcOlGGbCj1pueSjCoxvDoB8=\",\"审判程序\":\"二审\",\"案号\":\"（2017）渝05民终5781号\",\"法院名称\":\"重庆市第五中级人民法院\"},{\"裁判要旨段原文\":\"本院认为，原、被告签订的《汽车挂靠经营合同》系双方真实意思表示，且合同内容不违反法律法规的相关规定，该合同合法有效，对双方当事人均具有法律约束力，双方应按照合同的约定履行各自的义务。被告将涉案车辆挂靠在原告名下经营，应当按照合同约定及法律规定进行年检，并购买保\",\"不公开理由\":\"\",\"案件类型\":\"2\",\"裁判日期\":\"2017-09-27\",\"案件名称\":\"重庆尊远物流有限公司与令狐晓四挂靠经营合同纠纷一审民事判决书\",\"文书ID\":\"DcOORwHDgEAIADBLw4fChifDk8K/wqQ2CsKSw4LDncKsPlptFFTDrTXCjWrCh8KgSsK+WClaw5jCuwDDhFERDsKEdXDDisK9DRl7wqDDosOoI8K9wpDDq0hwO1t9bcOOIcOSwpPCtgHDpsK9NcO8bsOmw4rCksOww7nCs8KOZsKfw7ASwr8Vw5hTKBV7KsOTw4pBMMKVwpXDvUTDrsKFw7nDmMOfI8KEHQFmN8KeUMKmTsOaw4DCiXXCosKkw6Mew6DCpHFMw7sA\",\"审判程序\":\"一审\",\"案号\":\"（2017）渝0104民初2970号\",\"法院名称\":\"重庆市大渡口区人民法院\"}]"""
json_text_ret = json_text.replace('\\"', '\"')
print(json_text_ret)
page_data = json.loads(json_text_ret)  # 转移字符
ids = []
for data in page_data:
    if data.get("RunEval"):
        RunEval = data.get("RunEval")
        print("=====RunEval======")
        print(RunEval)
        print("==================")
    elif data.get("文书ID"):
        __data = data.get("文书ID");
        print(__data)
        ids.append(__data)

ret = decrypt_id_array(RunEval, ids)
print("********************")
for _id in ret.values():
    print(_id)
