

# ----------------------------------------------------------------------------------------------------
# 
# 此 方 法 是 打 开 某 一 个 作 者 的 主 页 ， 然 后 手 动 滑 动 实 现 获 取   j s o n   包
# 
# 比 较 初 级 ， 所 以  j s  o n   包 都 下载 在 了 同 一 个 文 本 之 中 ，比 较 不  舒 心
# 
# 解 析 文 本 ， 正 则 提 取 地 址 链 接  ，然 后 通 过  requests  去 下 载 视 频 
#  
# 可 以 后 期 跟 appium 结 合 实 现自 动 滑 动 及 下 载，详 细 见 另 一 个 my_appium 仓 库
# 
#----------------------------------------------------------------------------------------------------- 




#在fiddler中的 OnBeforeResponse 函数里插入一个保存json文件的操作。一但返回是json数据就保存
# static function OnBeforeResponse(oSession: Session) {
#   if (m_Hide304s & & oSession.responseCode == 304)
#      {
#     oSession["ui-hide"] = "true";
#            }
#
# if (oSession.uriContains("https://api-hl.amemv.com/aweme/v1/aweme/post/")){
#         var strBody=oSession.GetResponseBodyAsString();
#         var sps = oSession.PathAndQuery.slice(-58, );
#         // FiddlerObject.alert(sps)
#         var filename = "F:\\l1\\"+sps+".json";
#         var curDate = new Date();
#         var sw: System.IO.StreamWriter;
#         if
#         (System.IO.File.Exists(filename))
#         {
#             sw = System.IO.File.AppendText(filename);
#         sw.Write(strBody);
#         }
#         else {
#             sw = System.IO.File.CreateText(filename);
#         sw.Write(strBody);
#         }
#
#         sw.Close();
#         sw.Dispose();
#
#         }
#
#         }







import json
import re
import requests

# 打开json 文件
f=open('123.json','r',encoding='utf-8')
m=f.read()

# 正则提取框架
n=re.findall(""""play_addr":{"uri.*?D",""",m)
print(len(n))

# 小架构开始匹配地址
for i in n:

    ml=re.findall("""http.*?,""",i)

    # 查看匹配出的地址
    print(ml[0][:-2])

    # 新建视频文件
    f=open(ml[0][100:105]+".mp4","wb")

    # 请求地址并写入
    req=requests.get(ml[0][:-2])
    f.write(req.content)

    # 关闭文件
    f.close()
    print("下载完毕")
