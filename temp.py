import requests
import urllib
import json
import re


# a1 = """<ul class="popcitylist" style="overflow: auto; max-height: 280px; height: 191px; display: block;" method="hotData" id="ul_list1"><li class="ac_even openLi ac_odd" title="北京" data="BJP">北京</li><li class="ac_even openLi ac_odd" title="上海" data="SHH">上海</li><li class="ac_even openLi ac_odd" title="天津" data="TJP">天津</li><li class="ac_even openLi ac_odd" title="重庆" data="CQW">重庆</li><li class="ac_even openLi ac_odd" title="长沙" data="CSQ">长沙</li><li class="ac_even openLi ac_odd" title="长春" data="CCT">长春</li><li class="ac_even openLi ac_odd" title="成都" data="CDW">成都</li><li class="ac_even openLi ac_odd" title="福州" data="FZS">福州</li><li class="ac_even openLi ac_odd" title="广州" data="GZQ">广州</li><li class="ac_even openLi ac_odd" title="贵阳" data="GIW">贵阳</li><li class="ac_even openLi ac_odd" title="呼和浩特" data="HHC">呼和浩特</li><li class="ac_even openLi ac_odd" title="哈尔滨" data="HBB">哈尔滨</li><li class="ac_even openLi ac_odd" title="合肥" data="HFH">合肥</li><li class="ac_even openLi ac_odd" title="杭州" data="HZH">杭州</li><li class="ac_even openLi ac_odd" title="海口" data="VUQ">海口</li><li class="ac_even openLi ac_odd" title="济南" data="JNK">济南</li><li class="ac_even openLi ac_odd" title="昆明" data="KMM">昆明</li><li class="ac_even openLi ac_odd" title="拉萨" data="LSO">拉萨</li><li class="ac_even openLi ac_odd" title="兰州" data="LZJ">兰州</li><li class="ac_even openLi ac_odd" title="南宁" data="NNZ">南宁</li><li class="ac_even openLi ac_odd" title="南京" data="NJH">南京</li><li class="ac_even openLi ac_odd" title="南昌" data="NCG">南昌</li><li class="ac_even openLi ac_odd" title="沈阳" data="SYT">沈阳</li><li class="ac_even openLi ac_odd" title="石家庄" data="SJP">石家庄</li><li class="ac_even openLi ac_odd" title="太原" data="TYV">太原</li><li class="ac_even openLi ac_odd" title="乌鲁木齐南" data="WMR">乌鲁木齐南</li><li class="ac_even openLi ac_odd" title="武汉" data="WHN">武汉</li><li class="ac_even openLi ac_odd" title="西宁" data="XNO">西宁</li><li class="ac_even openLi ac_odd" title="西安" data="XAY">西安</li><li class="ac_even openLi ac_odd" title="银川" data="YIJ">银川</li><li class="ac_even openLi ac_odd" title="郑州" data="ZZF">郑州</li><li class="ac_even openLi ac_odd" title="深圳" data="SZQ">深圳</li><li class="ac_even openLi ac_odd" title="厦门" data="XMS">厦门</li></ul>"""
#
# a2 = """<div id="ul_list2" style="height: 0px; display: none;"><ul class="popcitylist" style="overflow: auto; max-height: 260px; display: none;"><li class="ac_letter">A</li><li class="ac_even openLi ac_odd" title="阿尔山" data="ART">阿尔山</li><li class="ac_even openLi ac_odd" title="安康" data="AKY">安康</li><li class="ac_even openLi ac_odd" title="阿克苏" data="ASR">阿克苏</li><li class="ac_even openLi ac_odd" title="阿里河" data="AHX">阿里河</li><li class="ac_even openLi ac_odd" title="阿拉山口" data="AKR">阿拉山口</li><li class="ac_even openLi ac_odd" title="安平" data="APT">安平</li><li class="ac_even openLi ac_odd" title="安庆" data="AQH">安庆</li><li class="ac_even openLi ac_odd" title="安顺" data="ASW">安顺</li><li class="ac_even openLi ac_odd" title="鞍山" data="AST">鞍山</li><li class="ac_even openLi ac_odd" title="安阳" data="AYF">安阳</li><li class="ac_even openLi ac_odd" title="昂昂溪" data="AAX">昂昂溪</li><li class="ac_even openLi ac_odd" title="阿城" data="ACB">阿城</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; display: none;"><li class="ac_letter">B</li><li class="ac_even openLi ac_odd" title="北京北" data="VAP">北京北</li><li class="ac_even openLi ac_odd" title="北京东" data="BOP">北京东</li><li class="ac_even openLi ac_odd" title="北京" data="BJP">北京</li><li class="ac_even openLi ac_odd" title="北京南" data="VNP">北京南</li><li class="ac_even openLi ac_odd" title="北京西" data="BXP">北京西</li><li class="ac_even openLi ac_odd" title="北安" data="BAB">北安</li><li class="ac_even openLi ac_odd" title="蚌埠" data="BBH">蚌埠</li><li class="ac_even openLi ac_odd" title="白城" data="BCT">白城</li><li class="ac_even openLi ac_odd" title="北海" data="BHZ">北海</li><li class="ac_even openLi ac_odd" title="白河" data="BEL">白河</li><li class="ac_even openLi ac_odd" title="白涧" data="BAP">白涧</li><li class="ac_even openLi ac_odd" title="宝鸡" data="BJY">宝鸡</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; display: none;"><li class="ac_letter">C</li><li class="ac_even openLi ac_odd" title="重庆北" data="CUW">重庆北</li><li class="ac_even openLi ac_odd" title="重庆" data="CQW">重庆</li><li class="ac_even openLi ac_odd" title="重庆南" data="CRW">重庆南</li><li class="ac_even openLi ac_odd" title="长春" data="CCT">长春</li><li class="ac_even openLi ac_odd" title="长春南" data="CET">长春南</li><li class="ac_even openLi ac_odd" title="长春西" data="CRT">长春西</li><li class="ac_even openLi ac_odd" title="成都东" data="ICW">成都东</li><li class="ac_even openLi ac_odd" title="成都南" data="CNW">成都南</li><li class="ac_even openLi ac_odd" title="成都" data="CDW">成都</li><li class="ac_even openLi ac_odd" title="长沙" data="CSQ">长沙</li><li class="ac_even openLi ac_odd" title="长沙南" data="CWQ">长沙南</li><li class="ac_even openLi ac_odd" title="赤壁" data="CBN">赤壁</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; display: none;"><li class="ac_letter">D</li><li class="ac_even openLi ac_odd" title="大安北" data="RNT">大安北</li><li class="ac_even openLi ac_odd" title="大成" data="DCT">大成</li><li class="ac_even openLi ac_odd" title="丹东" data="DUT">丹东</li><li class="ac_even openLi ac_odd" title="东方红" data="DFB">东方红</li><li class="ac_even openLi ac_odd" title="东莞东" data="DMQ">东莞东</li><li class="ac_even openLi ac_odd" title="大虎山" data="DHD">大虎山</li><li class="ac_even openLi ac_odd" title="敦煌" data="DHJ">敦煌</li><li class="ac_even openLi ac_odd" title="敦化" data="DHL">敦化</li><li class="ac_even openLi ac_odd" title="德惠" data="DHT">德惠</li><li class="ac_even openLi ac_odd" title="东京城" data="DJB">东京城</li><li class="ac_even openLi ac_odd" title="大涧" data="DFP">大涧</li><li class="ac_even openLi ac_odd" title="都江堰" data="DDW">都江堰</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; display: none;"><li class="ac_letter">E</li><li class="ac_even openLi ac_odd" title="额济纳" data="EJC">额济纳</li><li class="ac_even openLi ac_odd" title="二连" data="RLC">二连</li><li class="ac_even openLi ac_odd" title="恩施" data="ESN">恩施</li><li class="ac_even openLi ac_odd" title="峨边" data="EBW">峨边</li><li class="ac_even openLi ac_odd" title="二道沟门" data="RDP">二道沟门</li><li class="ac_even openLi ac_odd" title="二道湾" data="RDX">二道湾</li><li class="ac_even openLi ac_odd" title="鄂尔多斯" data="EEC">鄂尔多斯</li><li class="ac_even openLi ac_odd" title="二龙" data="RLD">二龙</li><li class="ac_even openLi ac_odd" title="二龙山屯" data="ELA">二龙山屯</li><li class="ac_even openLi ac_odd" title="峨眉" data="EMW">峨眉</li><li class="ac_even openLi ac_odd" title="二密河" data="RML">二密河</li><li class="ac_even openLi ac_odd" title="二营" data="RYJ">二营</li></ul></div>"""
# a3 = """<div id="ul_list3" style="height: 270px; display: none;"><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">F</li><li class="ac_even openLi" title="福州" data="FZS">福州</li><li class="ac_even openLi" title="福州南" data="FYS">福州南</li><li class="ac_even openLi" title="福鼎" data="FES">福鼎</li><li class="ac_even openLi" title="凤凰机场" data="FJQ">凤凰机场</li><li class="ac_even openLi" title="风陵渡" data="FLV">风陵渡</li><li class="ac_even openLi" title="涪陵" data="FLW">涪陵</li><li class="ac_even openLi" title="富拉尔基" data="FRX">富拉尔基</li><li class="ac_even openLi" title="抚顺北" data="FET">抚顺北</li><li class="ac_even openLi" title="佛山" data="FSQ">佛山</li><li class="ac_even openLi" title="阜新南" data="FXD">阜新南</li><li class="ac_even openLi" title="阜阳" data="FYH">阜阳</li><li class="ac_even openLi" title="福安" data="FAS">福安</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">G</li><li class="ac_even openLi" title="广州南" data="IZQ">广州南</li><li class="ac_even openLi" title="广州东" data="GGQ">广州东</li><li class="ac_even openLi" title="贵阳" data="GIW">贵阳</li><li class="ac_even openLi" title="广州" data="GZQ">广州</li><li class="ac_even openLi" title="广州西" data="GXQ">广州西</li><li class="ac_even openLi" title="格尔木" data="GRO">格尔木</li><li class="ac_even openLi" title="广汉" data="GHW">广汉</li><li class="ac_even openLi" title="古交" data="GJV">古交</li><li class="ac_even openLi" title="桂林北" data="GBZ">桂林北</li><li class="ac_even openLi" title="古莲" data="GRX">古莲</li><li class="ac_even openLi" title="桂林" data="GLZ">桂林</li><li class="ac_even openLi" title="固始" data="GXN">固始</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">H</li><li class="ac_even openLi" title="哈尔滨" data="HBB">哈尔滨</li><li class="ac_even openLi" title="哈尔滨东" data="VBB">哈尔滨东</li><li class="ac_even openLi" title="哈尔滨西" data="VAB">哈尔滨西</li><li class="ac_even openLi" title="合肥" data="HFH">合肥</li><li class="ac_even openLi" title="合肥西" data="HTH">合肥西</li><li class="ac_even openLi" title="呼和浩特东" data="NDC">呼和浩特东</li><li class="ac_even openLi" title="呼和浩特" data="HHC">呼和浩特</li><li class="ac_even openLi" title="海  口东" data="KEQ">海  口东</li><li class="ac_even openLi" title="海口东" data="HMQ">海口东</li><li class="ac_even openLi" title="海口" data="VUQ">海口</li><li class="ac_even openLi" title="杭州东" data="HGH">杭州东</li><li class="ac_even openLi" title="杭州" data="HZH">杭州</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">J</li><li class="ac_even openLi" title="济南" data="JNK">济南</li><li class="ac_even openLi" title="济南东" data="JAK">济南东</li><li class="ac_even openLi" title="济南西" data="JGK">济南西</li><li class="ac_even openLi" title="吉安" data="VAG">吉安</li><li class="ac_even openLi" title="集安" data="JAL">集安</li><li class="ac_even openLi" title="江边村" data="JBG">江边村</li><li class="ac_even openLi" title="晋城" data="JCF">晋城</li><li class="ac_even openLi" title="金城江" data="JJZ">金城江</li><li class="ac_even openLi" title="景德镇" data="JCG">景德镇</li><li class="ac_even openLi" title="嘉峰" data="JFF">嘉峰</li><li class="ac_even openLi" title="加格达奇" data="JGX">加格达奇</li><li class="ac_even openLi" title="井冈山" data="JGG">井冈山</li></ul></div>"""
# a4 = """<div id="ul_list4" style="height: 270px; display: none;"><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">K</li><li class="ac_even openLi" title="昆明" data="KMM">昆明</li><li class="ac_even openLi" title="昆明西" data="KXM">昆明西</li><li class="ac_even openLi" title="库尔勒" data="KLR">库尔勒</li><li class="ac_even openLi" title="开封" data="KFF">开封</li><li class="ac_even openLi" title="岢岚" data="KLV">岢岚</li><li class="ac_even openLi" title="凯里" data="KLW">凯里</li><li class="ac_even openLi" title="喀什" data="KSR">喀什</li><li class="ac_even openLi" title="昆山南" data="KNH">昆山南</li><li class="ac_even openLi" title="奎屯" data="KTR">奎屯</li><li class="ac_even openLi" title="开原" data="KYT">开原</li><li class="ac_even openLi" title="开安" data="KAT">开安</li><li class="ac_even openLi" title="库车" data="KCR">库车</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">L</li><li class="ac_even openLi" title="拉萨" data="LSO">拉萨</li><li class="ac_even openLi" title="兰州东" data="LVJ">兰州东</li><li class="ac_even openLi" title="兰州" data="LZJ">兰州</li><li class="ac_even openLi" title="兰州西" data="LAJ">兰州西</li><li class="ac_even openLi" title="六安" data="UAH">六安</li><li class="ac_even openLi" title="灵宝" data="LBF">灵宝</li><li class="ac_even openLi" title="芦潮港" data="UCH">芦潮港</li><li class="ac_even openLi" title="隆昌" data="LCW">隆昌</li><li class="ac_even openLi" title="陆川" data="LKZ">陆川</li><li class="ac_even openLi" title="利川" data="LCN">利川</li><li class="ac_even openLi" title="临川" data="LCG">临川</li><li class="ac_even openLi" title="潞城" data="UTP">潞城</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">M</li><li class="ac_even openLi" title="麻城" data="MCN">麻城</li><li class="ac_even openLi" title="免渡河" data="MDX">免渡河</li><li class="ac_even openLi" title="牡丹江" data="MDB">牡丹江</li><li class="ac_even openLi" title="莫尔道嘎" data="MRX">莫尔道嘎</li><li class="ac_even openLi" title="明光" data="MGH">明光</li><li class="ac_even openLi" title="满归" data="MHX">满归</li><li class="ac_even openLi" title="漠河" data="MVX">漠河</li><li class="ac_even openLi" title="茂名" data="MDQ">茂名</li><li class="ac_even openLi" title="茂名西" data="MMZ">茂名西</li><li class="ac_even openLi" title="密山" data="MSB">密山</li><li class="ac_even openLi" title="马三家" data="MJT">马三家</li><li class="ac_even openLi" title="麻尾" data="VAW">麻尾</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">N</li><li class="ac_even openLi" title="南昌" data="NCG">南昌</li><li class="ac_even openLi" title="南京" data="NJH">南京</li><li class="ac_even openLi" title="南京南" data="NKH">南京南</li><li class="ac_even openLi" title="南宁" data="NNZ">南宁</li><li class="ac_even openLi" title="宁波东" data="NVH">宁波东</li><li class="ac_even openLi" title="宁波" data="NGH">宁波</li><li class="ac_even openLi" title="南岔" data="NCB">南岔</li><li class="ac_even openLi" title="南充" data="NCW">南充</li><li class="ac_even openLi" title="南丹" data="NDZ">南丹</li><li class="ac_even openLi" title="南大庙" data="NMP">南大庙</li><li class="ac_even openLi" title="南芬" data="NFT">南芬</li><li class="ac_even openLi" title="讷河" data="NHX">讷河</li></ul></div>"""
# a5 = """<div id="ul_list5" style="height: 270px; display: none;"><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">P</li><li class="ac_even openLi" title="平顶山" data="PEN">平顶山</li><li class="ac_even openLi" title="盘锦" data="PVD">盘锦</li><li class="ac_even openLi" title="平凉" data="PIJ">平凉</li><li class="ac_even openLi" title="平凉南" data="POJ">平凉南</li><li class="ac_even openLi" title="平泉" data="PQP">平泉</li><li class="ac_even openLi" title="坪石" data="PSQ">坪石</li><li class="ac_even openLi" title="萍乡" data="PXG">萍乡</li><li class="ac_even openLi" title="凭祥" data="PXZ">凭祥</li><li class="ac_even openLi" title="郫县西" data="PCW">郫县西</li><li class="ac_even openLi" title="攀枝花" data="PRW">攀枝花</li><li class="ac_even openLi" title="蓬安" data="PAW">蓬安</li><li class="ac_even openLi" title="平安" data="PAL">平安</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">Q</li><li class="ac_even openLi" title="蕲春" data="QRN">蕲春</li><li class="ac_even openLi" title="青城山" data="QSW">青城山</li><li class="ac_even openLi" title="青岛" data="QDK">青岛</li><li class="ac_even openLi" title="清河城" data="QYP">清河城</li><li class="ac_even openLi" title="曲靖" data="QJM">曲靖</li><li class="ac_even openLi" title="黔江" data="QNW">黔江</li><li class="ac_even openLi" title="前进镇" data="QEB">前进镇</li><li class="ac_even openLi" title="齐齐哈尔" data="QHX">齐齐哈尔</li><li class="ac_even openLi" title="七台河" data="QTB">七台河</li><li class="ac_even openLi" title="沁县" data="QVV">沁县</li><li class="ac_even openLi" title="泉州东" data="QRS">泉州东</li><li class="ac_even openLi" title="泉州" data="QYS">泉州</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">R</li><li class="ac_even openLi" title="融安" data="RAZ">融安</li><li class="ac_even openLi" title="汝箕沟" data="RQJ">汝箕沟</li><li class="ac_even openLi" title="瑞金" data="RJG">瑞金</li><li class="ac_even openLi" title="日照" data="RZK">日照</li><li class="ac_even openLi" title="瑞安" data="RAH">瑞安</li><li class="ac_even openLi" title="荣昌" data="RCW">荣昌</li><li class="ac_even openLi" title="瑞昌" data="RCG">瑞昌</li><li class="ac_even openLi" title="如皋" data="RBH">如皋</li><li class="ac_even openLi" title="容桂" data="RUQ">容桂</li><li class="ac_even openLi" title="任丘" data="RQP">任丘</li><li class="ac_even openLi" title="乳山" data="ROK">乳山</li><li class="ac_even openLi" title="融水" data="RSZ">融水</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">S</li><li class="ac_even openLi" title="上海" data="SHH">上海</li><li class="ac_even openLi" title="上海南" data="SNH">上海南</li><li class="ac_even openLi" title="上海虹桥" data="AOH">上海虹桥</li><li class="ac_even openLi" title="上海西" data="SXH">上海西</li><li class="ac_even openLi" title="石家庄北" data="VVP">石家庄北</li><li class="ac_even openLi" title="石家庄" data="SJP">石家庄</li><li class="ac_even openLi" title="沈阳" data="SYT">沈阳</li><li class="ac_even openLi" title="沈阳北" data="SBT">沈阳北</li><li class="ac_even openLi" title="沈阳东" data="SDT">沈阳东</li><li class="ac_even openLi" title="双城堡" data="SCB">双城堡</li><li class="ac_even openLi" title="绥芬河" data="SFB">绥芬河</li><li class="ac_even openLi" title="韶关东" data="SGQ">韶关东</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">T</li><li class="ac_even openLi" title="天津北" data="TBP">天津北</li><li class="ac_even openLi" title="天津" data="TJP">天津</li><li class="ac_even openLi" title="天津南" data="TIP">天津南</li><li class="ac_even openLi" title="天津西" data="TXP">天津西</li><li class="ac_even openLi" title="太原北" data="TBV">太原北</li><li class="ac_even openLi" title="太原东" data="TDV">太原东</li><li class="ac_even openLi" title="太原" data="TYV">太原</li><li class="ac_even openLi" title="塘豹" data="TBQ">塘豹</li><li class="ac_even openLi" title="塔尔气" data="TVX">塔尔气</li><li class="ac_even openLi" title="潼关" data="TGY">潼关</li><li class="ac_even openLi" title="塘沽" data="TGP">塘沽</li><li class="ac_even openLi" title="塔河" data="TXX">塔河</li></ul></div>"""
# a6 = """<div id="ul_list6" style="height: 270px; display: block;"><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">W</li><li class="ac_even openLi" title="武汉" data="WHN">武汉</li><li class="ac_even openLi" title="王家营西" data="KNM">王家营西</li><li class="ac_even openLi" title="乌鲁木齐南" data="WMR">乌鲁木齐南</li><li class="ac_even openLi" title="五常" data="WCB">五常</li><li class="ac_even openLi" title="武昌" data="WCN">武昌</li><li class="ac_even openLi" title="瓦房店" data="WDT">瓦房店</li><li class="ac_even openLi" title="威海" data="WKK">威海</li><li class="ac_even openLi" title="芜湖" data="WHH">芜湖</li><li class="ac_even openLi" title="乌海西" data="WXC">乌海西</li><li class="ac_even openLi" title="吴家屯" data="WJT">吴家屯</li><li class="ac_even openLi" title="武隆" data="WLW">武隆</li><li class="ac_even openLi" title="乌兰浩特" data="WWT">乌兰浩特</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">X</li><li class="ac_even openLi" title="西安北" data="EAY">西安北</li><li class="ac_even openLi" title="西安" data="XAY">西安</li><li class="ac_even openLi" title="西安南" data="CAY">西安南</li><li class="ac_even openLi" title="西宁" data="XNO">西宁</li><li class="ac_even openLi" title="西昌" data="ECW">西昌</li><li class="ac_even openLi" title="许昌" data="XCF">许昌</li><li class="ac_even openLi" title="西昌南" data="ENW">西昌南</li><li class="ac_even openLi" title="香坊" data="XFB">香坊</li><li class="ac_even openLi" title="轩岗" data="XGV">轩岗</li><li class="ac_even openLi" title="兴国" data="EUG">兴国</li><li class="ac_even openLi" title="宣汉" data="XHY">宣汉</li><li class="ac_even openLi" title="新会" data="EFQ">新会</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">Y</li><li class="ac_even openLi" title="银川" data="YIJ">银川</li><li class="ac_even openLi" title="延安" data="YWY">延安</li><li class="ac_even openLi" title="宜宾" data="YBW">宜宾</li><li class="ac_even openLi" title="亚布力南" data="YWB">亚布力南</li><li class="ac_even openLi" title="叶柏寿" data="YBD">叶柏寿</li><li class="ac_even openLi" title="宜昌东" data="HAN">宜昌东</li><li class="ac_even openLi" title="永川" data="YCW">永川</li><li class="ac_even openLi" title="盐城" data="AFH">盐城</li><li class="ac_even openLi" title="宜昌" data="YCN">宜昌</li><li class="ac_even openLi" title="运城" data="YNV">运城</li><li class="ac_even openLi" title="伊春" data="YCB">伊春</li><li class="ac_even openLi" title="榆次" data="YCV">榆次</li></ul><ul class="popcitylist" style="overflow: auto; max-height: 260px; "><li class="ac_letter">Z</li><li class="ac_even openLi" title="郑州" data="ZZF">郑州</li><li class="ac_even openLi" title="淄博" data="ZBK">淄博</li><li class="ac_even openLi" title="镇城底" data="ZDV">镇城底</li><li class="ac_even openLi" title="自贡" data="ZGW">自贡</li><li class="ac_even openLi" title="珠海" data="ZHQ">珠海</li><li class="ac_even openLi" title="珠海北" data="ZIQ">珠海北</li><li class="ac_even openLi" title="湛江" data="ZJZ">湛江</li><li class="ac_even openLi" title="镇江" data="ZJH">镇江</li><li class="ac_even openLi" title="张家界" data="DIQ">张家界</li><li class="ac_even openLi" title="张家口" data="ZKP">张家口</li><li class="ac_even openLi" title="张家口南" data="ZMP">张家口南</li><li class="ac_even openLi" title="周口" data="ZKN">周口</li></ul></div>"""
#
# ff = [a1, a2, a3, a4, a5, a6]
#
#
# def process_info(s):
#     result = {}
#     for a in s:
#         c = []
#         v = re.split(r'</li>?', a)
#         for i in v:
#             try:
#                 n = i.split('data=')[1]
#             except:
#                 n = None
#             if n:
#                 c.append(n)
#
#         temp_d = {}
#         for i in c:
#             print(i, 'i')
#             k = i.split(">")[0].strip("'").strip('"')
#             v = i.split(">")[1].strip("'").strip('"')
#             temp_d[v] = k
#         result.update(temp_d)
#     return result
#
# new = []
# a = ['ZKX565Ej2b2gcVSnZ7ce4fV7BtOUorsZU7kIRTkArhsun1ZDan9zEf4BkOWO7I663rAO4FNDmhJg%0A5%2BDoacnWwEZHiP291JyiHbV4VMXWLbUScGFoXStIzDfNVtsIPKjU%2FfYhxFqcpzgFTV%2F8jY0FEJiB%0APRU%2BgpyGHPujdvEzR%2BcLzAoCSCyBQoqTPLbxpjW10%2BNO4AxkodyvMoo0wtvgTdLxbSp7%2F%2BzJLqoL%0ALOI4%2Fuj2IciltY2%2F3g%3D%3D|预订|5800000Z600C|Z60|FZS|BXP|NCG|BXP|00:57|13:05|12:08|Y|0noJeN7Q%2BPhaLyWb3XPaBIHTqMNLcHAVFW%2F09UjoF1N3ZcGzVZ27QWtZ%2FRw%3D|20171219|3|G2|04|06|0|0||||无|||无||无|1|||||10401030|1413', '|预订|650000Z10804|Z108|SZQ|BXP|NCG|BXP|01:03|13:17|12:14|N|8sWWfrxDvyAyq1isH1Nmn6s68OdfdLSTNveLzyyPidxqJGK%2FGYrWROMIlFU%3D|20171219|3|Q9|05|10|0|0||||无|||无||无|无|||||10401030|1413', '%2BKD2cL9k0o0uAZRzBEVBboYpyfLrDobPhKo2YQ12MXrzJLZ1yN8RoxaYOFuKUM6Hw9lj12P%2B6C%2Bi%0AheukMu2fOVAqGEupSSuzjbKE0RmZk7HxZAksKbNS3MruNAq02jL5%2FmOTPzSgg0G73IrD5qrjJwnJ%0AL%2BOPrz3nBsET%2BmV61kchiXEM7vnJGFBPSDCtNV1PemjmJbcTzmweMcRMSZE2M6MCD29GdVD74AgV%0AXCSXsEI%3D|预订|5u00000G380E|G38|NXG|VNP|NXG|VNP|08:30|17:57|09:27|Y|wPZLhMYHB32CpwZTCQ0vCe4OXPtvQc1TjF8I0czptJYXptDS|20171220|3|G1|01|20|1|0|||||||||||有|有|5||O0M090|OM9', 'nI0%2FzqNaE9jt%2BQ329RJEtFlT55SwjMH1NsbYUpf1i4oCkS3bj0FK1h%2Fsc0Jh5mpkLMd43yJLBgHs%0AITC8NBHs1wktoFoUIm%2FL2dBPJ0XTUpk5YDE%2BvnQwqGQ%2FuTI0644lgR%2Fyqkfb3yUVzKILJuI6TENM%0AEc5P5FDXVPuKkoGPWW9ymvGXz0KgMK2b%2BqOHXFXj0tCEc5fRgoJPAda%2Fghn7tbF%2BV6kfYdeVIcF3%0AA%2BiNcq8%3D|预订|5u0000G48800|G488|NXG|BXP|NXG|BXP|10:49|17:06|06:17|Y|AmNPTnwhvWK9p6%2FwGGypnhXVOyT7VQrkw8%2FnQPUcNRL3Znuz|20171220|3|G1|01|08|1|0|||||||||||有|3|无||O0M090|OM9', 'n95Aslw9XBDQIwVHFzz5IJcom1goG36i%2F0ifbI2KolTKEhkSz%2B%2FQgct5VMqkMgm4JQR4LMKKLwiC%0A2HTy5U1kzIlUkL30KbAuA%2BQPkrb6pG3gAoY4DQPk48u3umeTO3ePsiiQFgNzjfNFG2HYTmesIvDL%0A16psPWPW8H1Mw9zvr1N5GTB56L9OTqBR7Zf2PqQ477%2BMDZ9QX%2FpJ4Nw23MwOKmw%2F5moXara70cS8%0AMt9X4VMi26pz|预订|570000T1470E|T147|NCG|BJP|NCG|BJP|12:10|10:52|22:42|Y|kx%2FXDGH%2FShwstEWGUjJVvWBzPdsGKDDLxO009g0whUFMd24kRKDNCKTudj8%3D|20171220|3|G1|01|20|0|0||||3|||无||无|有|||||10401030|1413', 'XX6pq3zUGfLp2vqyUMCCgmIUVVgLZeBW3CXBtzh9Qm6DJQAnYBxpfAC7D8Zzr9g%2BH5VAH%2F3s7YTD%0AtY4H4OdxempLPyeudUaz8q%2B96V%2Fqdv%2FAcZ1M4P9Ovjz2041OmLae4ABbB01wq3MqQ4bUbiZxYa%2BR%0AQtyAhR7bLv25zJarRTC1iNMkNP7vpSFfyJGA%2FDK84epXgPY9eRTC62y7jQvlCY7Z9xfeBc6YMDCU%0AMHbAYH8%3D|预订|5u0000G49200|G492|NXG|BXP|NXG|BXP|14:45|22:42|07:57|Y|ECtWGqMGm8IEzfR9h8u51C9IOr2lxki4P8JGqr5hVpMM%2BSIM|20171220|3|G1|01|12|1|0||||||12|||||有|有|||O0M0P0|OMP', 'v36E49%2F2nAJbNJG9zH6RoGs7Dopqh4HxdQvYxLZwyiM%2FmmIWSwX%2BwD28o0wkli763mSxZxWowJEE%0AN2y7bGKaxHKSMItaghCK3cqfm4s7fyvM5cDzPOv65YV64wNT%2BjJ2A9D3%2BpcjuG6xbz%2F0J3s6pPZB%0AcUJkFGIGJv0I7Vb70juhDUVe8Jh6O%2BhKJSbVHKypbMGhjUOKacboYJNuLzvmUzAAeijyqK52R72r%0ABIg%2FpEXluqcbgbFe%2BQ%3D%3D|预订|57000K14540C|K1454|GZG|BXP|NCG|BXP|16:40|11:21|18:41|Y|KrPGX1YjCXohB5mw%2Ft%2FIKa5jM7bug1BlwhEH9ihx6HuOBHecfFtfMfHpt0Q%3D|20171220|3|G2|06|26|0|0||||4|||无||无|有|||||10401030|1413', 'gAH9rzespo6wMaf%2Fr2QQGi6TKoNUNmnAyrfofKwv0BXYQr%2FRbT%2Bxns2aDADlAxmUVlgJvk%2Bs%2FJYA%0A8yAJQpTLA3wx1z9DOPHE%2BLDK5Re7fuPXsIt2HxDkc48uivtrwRQrJFP7OpV8kRVcaxXMS48IxGMh%0AivymhwJwYK0nIhQg4OT1uUaHXQjtFopIBJKV75n45jjPEzPgHf8tz4AZy8q2wgMBi7xN%2FV2%2FOeug%0ADaXdLOoL3W1iiMCBKQ%3D%3D|预订|5u00000Z7204|Z72|SHS|BJP|NXG|BJP|17:42|06:28|12:46|Y|O8Vlj8PR3RtgZEWOMNReSQzeCnc6XOC5HrCR%2FNUO%2FAQA%2BOON68qoVxIUI7s%3D|20171220|3|G1|04|11|0|0||||无|||无||无|有|||||10401030|1413', 'GC0d2%2BVtl3TNGTupC7%2BnmL1aDc%2F2CeLcvDBYGwuwLHBXSGV47qmwD%2Bnxmj3L9Mfwv07xXpUzet7F%0A5ILFEQBvB3nbwd3UODRWYb1piIzeWoctgr7FEihny8RKDs2XUjfGFuWTfVZVytcczGRcil42kr74%0AWrQKeiNpZIOhW%2FHxwcu3MCRmoCRy4Y14nAWMXkOPv1SblWtzYjNK8Z0854OtawmCnmWwUnAPRPxM%0AnsWOJLTJCxmxDShL0g%3D%3D|预订|570000T1680G|T168|NCG|BXP|NCG|BXP|19:20|13:05|17:45|Y|cA%2FNW19wdV%2B5VGsNAU%2ByQ4JX1gZpcER%2BZzKwwbsDYyCvlrlFWrr1M9tlDgE%3D|20171220|3|G1|01|18|0|0||||无|||无||无|有|||||10401030|1413', 'c8osCTFbTo%2Br7WYnmBexQpf4tRtxVGTiM8OPTFSHuVtELuim42if2IYA1pAA5dXHP7iaNwDttFZ8%0AZId1CNQMDZOx0oatb1oEgBaZiMbBD5ns%2BM65ZZq14D6D4u8QxYOzM%2Fik3G6HhSAw%2FL1ITphChImc%0AP3VMy4qSmkpEFqjGZ%2BkgpbIYLBz5ltl2eMhj3etimZva8i3xa7C1VHYl%2Fza27WmSPzP4KfPOq4bE%0A2LLrvJPrzDUCymQsuj1%2FrzBsTiXT|预订|5700000Z660E|Z66|NCG|BXP|NCG|BXP|19:35|07:40|12:05|Y|fBO9usYOoWCTGoubC0GEEqdjxHmVfhLbGGaD1AjAgRqm%2FlkrpRrG0MT6R%2BcqcmPGqFP7kyKkgLs%3D|20171220|3|G1|01|03|0|0||8||3|||无||有|有|||||1040106030|14163', 'nR2sctxsFu%2B1Htzn%2BrDCK3I8Zq3dM4AGyB1nkf6iVWVmJSIXZ%2BbWHDcXafPZCZt8LNMo0QweHfpx%0A4lzCKMUvdw7ZVsc7%2FGDV6eg5J2YwS%2BPGu3RCavlNEtX%2BjV5oucAIjKNTpROGo8cn7R%2B%2FRTWyl31a%0AgCGjYgabmlWFCZ8xTdl4%2FdkOS0AWzoNk1BvhPcA23IK0kZ0gKw4khutqVf6%2BEQN7NbNWDHkUsM6a%0AwnOkwMxzZYFb5DpF2hzAM9lY900W|预订|5700000Z680G|Z68|NCG|BXP|NCG|BXP|19:42|07:48|12:06|Y|i231NvF2DmiV%2B6sl43tMAcbmBY3gcflH%2BhkxLRpKSLEVlJekam2QMBIm5TROeLcBVsJQL3GJP%2BQ%3D|20171220|3|G1|01|04|0|0||8||3|||无||有|有|||||1040106030|14163', 'ZYx5OHX3PPzU6RnWhMHreQZsHSAQ%2BhT8yURhIj9TFaYJLHpLfvAzKUJ5RuQZdrekpNcI%2BBUwWzIy%0ANj0ta0tRL66ww0R7O03ntFXDEmOXH9oOx5hzerQuXdCwYW2%2FWYkdhMU981nvlZxTESrL%2FXMb474m%0AWHd5UyyKfKJ5jq4opHXTdn39eVLhoCNPWuondGqoG%2Fx4i%2FgVIbwK%2BlgfO7kNsYm9ncAPPf8dK1MM%0AZWGs2WyyWg%2FMOc4ya7sR28x3CZoSeW8WCw%3D%3D|预订|570000Z1340H|Z134|JGG|BXP|NXG|BXP|19:53|08:03|12:10|Y|CbbmknVTkc44R4HObluKH6FdBhFrMr9jk22%2FsEC55zx1b5zukmdGTx%2F3ga1Ah11VW0lpfKbo8x8%3D|20171220|3|G2|03|06|0|0||1||无|||无||无|有|||||1040601030|14613', 'DMYvojSRIn0ZJ%2ByfZS4S%2B9JyzQo1HACuRKoEAWE0ZYeR%2BJD3%2Br0kftrs65jCSZtbWwfKZUeEnLrN%0A%2BTVJgUc9Vhz5PLtnEXq7DjfPeHu%2FJ8QhaydsNCZkkq77LJZfUcb8C5JlYDvgKZHcD2B%2BjICJODOY%0AHD4MoVDLQJprdiPXn5X%2FkYZnho%2FG7ASazqem40j2nUJsCJLm%2BFYdxMdy%2BnLwhDgJANfpoT4aBr4g%0AxADLuPpdaD%2FV0n52%2Fg%3D%3D|预订|580000K57209|K572|XMS|BXP|NCG|BXP|20:08|12:56|16:48|Y|7quBCuNnFZs3N7h0QFNyvdjCJUa6sPOU6S%2Bx8zOKCd5cXQzgHL9wsWcQLCk%3D|20171220|3|G2|12|21|0|0||||无|||无||无|有|||||10401030|1413', '14wrlL%2B1%2FsXbcdfYNUep60ZNjv%2Bab8KKNBV74bt0II8K8jDX7Zd4wLtoNdM%2F2j614hDTSj8d3LAR%0AWo8rOo5Cz4aimGSuNrbC0Yq%2FYegB4r4h8MkM%2FRplE18I5b8T2B491H5nIozCktBHPmNWe6T1UAAL%0AJ6Cyt71IQ3bmjVtach3H7Z0BNIV2WKAVzP6ywUq8Gcpsjje1V9YWWo4xzmJ0OrnGOY2TTjJDfOPm%0AeB1lXrx%2FO056AJnHQQ%3D%3D|预订|650000K1060T|K106|SZQ|BXP|NCG|BXP|22:45|16:25|17:40|Y|aXZN0bA5h7EOdza8gVCS1hFTRETEotmgx5hE59AUwvVl8FWj5%2FKNWIT65sg%3D|20171220|3|Q7|10|26|0|0||||2|||无||有|有|||||10401030|1413', 'm4uaiOGduJnrVS8mo%2FxZ47pig086IfAVorg1bmlKeEKQ%2BYaPfC9JCk8Fu%2BvH6Z%2BRPmm8qUBmjBvV%0AmgmJcMRXDfiMYvTEt%2FZJMTQPxuVoBFMS%2F4fo4%2Bv%2FUVZ9TDvtCY6RGT1AldTf6my%2B0n5vmoislHey%0Ay1zQuRgrhmUTfKw8XAJqN%2FzdsPr9lySaQ%2Fk9cJi6v%2BobbWBK5nxSQS4IV8sA%2BvO6Z9HbrJzpDtPB%0A3bMRmIOuqItWNhb2KQ%3D%3D|预订|580000Z30804|Z308|XMS|BXP|NCG|BXP|23:48|12:06|12:18|Y|BIP8tUsNJiwmxpK9cquCiaFpCxMhJmzkayZQJ26ttfFvAhH4ZFxLxfOzBcQ%3D|20171220|3|G1|04|10|0|0||||1|||无||无|有|||||10401030|1413']
# for i in a:
#     # new.append(i.split('|')[12:])
#     new.append(i.split('|'))
#
# for i in new:
#     print(i, "\n")
# print(len(new[0]))


class TrainSchedule(object):
    def __init__(self, list_item):
        self.secret_str = list_item[0]
        self.book = list_item[1]
        self.train_number = list_item[2]
        self.train_code = list_item[3]
        self.start = list_item[4]
        self.end = list_item[5]
        self.from_station = list_item[6]
        self.destination = list_item[7]
        self.start_time = list_item[8]
        self.arrive_time = list_item[9]
        self.time_cost = list_item[10]
        self.available = list_item[11]
        self.price_info = list_item[12]
        self.start_train_code = list_item[13]
        self.train_seat_feature = list_item[14]
        self.location_code = list_item[15]
        self.from_station_no = list_item[16]
        self.to_station_no = list_item[17]
        self.is_support_card = list_item[18]
        self.controlled_train_flag = list_item[19]
        self.gg_num = list_item[20]
        self.gr_num = list_item[21]
        self.qt_num = list_item[22]
        self.rw_num = list_item[23]
        self.rz_num = list_item[24]
        self.tz_num = list_item[25]
        self.wz_num = list_item[26]
        self.yb_num = list_item[27]
        self.yw_num = list_item[28]
        self.yz_num = list_item[29]
        self.ze_num = list_item[30]
        self.zy_num = list_item[31]
        self.swz_num = list_item[32]
        self.srrb_num = list_item[33]
        self.yp_ex = list_item[34]
        self.seat_types = list_item[35]


a = []

for i in range(224):
    a.append('  ')




for i, e in enumerate(a):
    if i % 15 == 0:
        print(i)
        print('www')
        a[i] = '*'

for i, e in enumerate(a):
    if i % 15 == 14:
        a[i] = '*'

for i in range(15):
    a[i] = '* '
    a[-i] = '* '

step = 15
for i, e in enumerate(a):
    if (i + 1) % 15 == 0:
        print(e)
    else:
        print(e, end='')


(define (equal? li l2)
(define x (list l1))
(define y (list l2))
(cond ((eq? (car x) (car y))
(cond (equal))))
)











