import requests
import urllib
import json
import re

INIT_PAGE = r'http://dynamic.12306.cn/otn/board/init'
CHA_PT_PAGE = r'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.3120046807730822'
LOGIN_PATH = r"https://kyfw.12306.cn/passport/web/login"
CAPTCHA_CHECK_PATH = r"https://kyfw.12306.cn/passport/captcha/captcha-check"
UAUTH_PATH = r"https://kyfw.12306.cn/passport/web/auth/uamtk"
USER_LOGIN_PATH = r"https://kyfw.12306.cn/otn/login/userLogin"
UA_CLIENT_PATH = r"https://kyfw.12306.cn/otn/uamauthclient"
INIT_MY12306 = "https://kyfw.12306.cn/otn/index/initMy12306"
URL_UNKNOW = "https://kyfw.12306.cn/otn/leftTicket/query"
ADULT = "ADULT"


LOGIN_SITE_E = 'E'
ANSWER = 'answer'
LOGIN_SITE = 'login_site'
RAND = 'rand'
SJRAND = 'sjrand'
CAPTCHA_NAME = 'image.jpeg'

STATION_CODE = {
    '珠海': 'ZHQ', '牡丹江': 'MDB', '兴国': 'EUG', '佛山': 'FSQ', '福州': 'FZS', '榆次': 'YCV', '广汉': 'GHW', '安顺': 'ASW',
    '乌海西': 'WXC', '南京南': 'NKH', '黔江': 'QNW', '白河': 'BEL', '阜阳': 'FYH', '昆山南': 'KNH', '吴家屯': 'WJT', '长春': 'CCT',
    '库尔勒': 'KLR', '如皋': 'RBH', '曲靖': 'QJM', '塘豹': 'TBQ', '阿尔山': 'ART', '汝箕沟': 'RQJ', '长春南': 'CET', '鞍山': 'AST',
    '满归': 'MHX', '宁波东': 'NVH', '武昌': 'WCN', '抚顺北': 'FET', '大安北': 'RNT', '西昌南': 'ENW', '济南西': 'JGK', '福州南': 'FYS',
    '都江堰': 'DDW', '平安': 'PAL', '西宁': 'XNO', '宜昌': 'YCN', '瑞安': 'RAH', '天津北': 'TBP', '成都东': 'ICW', '永川': 'YCW',
    '马三家': 'MJT', '宜宾': 'YBW', '北京南': 'VNP', '拉萨': 'LSO', '隆昌': 'LCW', '六安': 'UAH', '深圳': 'SZQ', '天津南': 'TIP',
    '明光': 'MGH', '茂名': 'MDQ', '北京西': 'BXP', '免渡河': 'MDX', '哈尔滨': 'HBB', '乳山': 'ROK', '沈阳东': 'SDT', '芦潮港': 'UCH',
    '恩施': 'ESN', '容桂': 'RUQ', '古莲': 'GRX', '密山': 'MSB', '二道沟门': 'RDP', '敦化': 'DHL', '茂名西': 'MMZ', '奎屯': 'KTR',
    '二龙': 'RLD', '开原': 'KYT', '讷河': 'NHX', '青城山': 'QSW', '武隆': 'WLW', '丹东': 'DUT', '兰州': 'LZJ', '陆川': 'LKZ',
    '呼和浩特东': 'NDC', '安康': 'AKY', '敦煌': 'DHJ', '张家口': 'ZKP', '固始': 'GXN', '福安': 'FAS', '凯里': 'KLW', '蓬安': 'PAW',
    '北海': 'BHZ', '绥芬河': 'SFB', '开安': 'KAT', '前进镇': 'QEB', '白涧': 'BAP', '西安': 'XAY', '利川': 'LCN', '石家庄北': 'VVP',
    '轩岗': 'XGV', '广州西': 'GXQ', '景德镇': 'JCG', '郫县西': 'PCW', '平泉': 'PQP', '麻尾': 'VAW', '塔河': 'TXX', '北京': 'BJP',
    '东京城': 'DJB', '兰州东': 'LVJ', '风陵渡': 'FLV', '西安北': 'EAY', '平凉南': 'POJ', '金城江': 'JJZ', '南大庙': 'NMP', '二密河': 'RML',
    '井冈山': 'JGG', '开封': 'KFF', '广州南': 'IZQ', '淄博': 'ZBK', '长沙': 'CSQ', '凤凰机场': 'FJQ', '天津西': 'TXP', '盐城': 'AFH',
    '大虎山': 'DHD', '重庆': 'CQW', '亚布力南': 'YWB', '涪陵': 'FLW', '青岛': 'QDK', '长沙南': 'CWQ', '张家界': 'DIQ', '昆明西': 'KXM',
    '潼关': 'TGY', '荣昌': 'RCW', '镇江': 'ZJH', '伊春': 'YCB', '香坊': 'XFB', '乌兰浩特': 'WWT', '岢岚': 'KLV', '南丹': 'NDZ',
    '阿拉山口': 'AKR', '成都南': 'CNW', '二道湾': 'RDX', '南充': 'NCW', '蕲春': 'QRN', '平顶山': 'PEN', '东方红': 'DFB', '德惠': 'DHT',
    '桂林': 'GLZ', '长春西': 'CRT', '延安': 'YWY', '新会': 'EFQ', '天津': 'TJP', '漠河': 'MVX', '阿里河': 'AHX', '许昌': 'XCF',
    '北京东': 'BOP', '成都': 'CDW', '盘锦': 'PVD', '南昌': 'NCG', '威海': 'WKK', '海口东': 'HMQ', '大成': 'DCT', '蚌埠': 'BBH',
    '任丘': 'RQP', '王家营西': 'KNM', '重庆南': 'CRW', '二营': 'RYJ', '广州东': 'GGQ', '二龙山屯': 'ELA', '济南': 'JNK', '周口': 'ZKN',
    '乌鲁木齐南': 'WMR', '西安南': 'CAY', '安平': 'APT', '富拉尔基': 'FRX', '安阳': 'AYF', '合肥西': 'HTH', '海  口东': 'KEQ', '潞城': 'UTP',
    '湛江': 'ZJZ', '泉州东': 'QRS', '七台河': 'QTB', '东莞东': 'DMQ', '融水': 'RSZ', '五常': 'WCB', '瑞金': 'RJG', '上海南': 'SNH',
    '西昌': 'ECW', '宜昌东': 'HAN', '沁县': 'QVV', '大涧': 'DFP', '自贡': 'ZGW', '晋城': 'JCF', '太原东': 'TDV', '叶柏寿': 'YBD',
    '上海虹桥': 'AOH', '赤壁': 'CBN', '武汉': 'WHN', '阿城': 'ACB', '安庆': 'AQH', '福鼎': 'FES', '塘沽': 'TGP', '嘉峰': 'JFF',
    '韶关东': 'SGQ', '鄂尔多斯': 'EEC', '日照': 'RZK', '宁波': 'NGH', '攀枝花': 'PRW', '沈阳北': 'SBT', '广州': 'GZQ', '沈阳': 'SYT',
    '桂林北': 'GBZ', '阿克苏': 'ASR', '额济纳': 'EJC', '平凉': 'PIJ', '运城': 'YNV', '齐齐哈尔': 'QHX', '济南东': 'JAK', '宝鸡': 'BJY',
    '双城堡': 'SCB', '郑州': 'ZZF', '石家庄': 'SJP', '古交': 'GJV', '杭州东': 'HGH', '临川': 'LCG', '瓦房店': 'WDT', '太原': 'TYV',
    '清河城': 'QYP', '南芬': 'NFT', '呼和浩特': 'HHC', '哈尔滨西': 'VAB', '阜新南': 'FXD', '厦门': 'XMS', '二连': 'RLC', '上海西': 'SXH',
    '凭祥': 'PXZ', '灵宝': 'LBF', '融安': 'RAZ', '南岔': 'NCB', '杭州': 'HZH', '莫尔道嘎': 'MRX', '昂昂溪': 'AAX', '喀什': 'KSR',
    '贵阳': 'GIW', '瑞昌': 'RCG', '吉安': 'VAG', '海口': 'VUQ', '宣汉': 'XHY', '银川': 'YIJ', '重庆北': 'CUW', '塔尔气': 'TVX',
    '北京北': 'VAP', '泉州': 'QYS', '麻城': 'MCN', '南宁': 'NNZ', '集安': 'JAL', '镇城底': 'ZDV', '上海': 'SHH', '坪石': 'PSQ',
    '峨边': 'EBW', '芜湖': 'WHH', '加格达奇': 'JGX', '白城': 'BCT', '哈尔滨东': 'VBB', '南京': 'NJH', '珠海北': 'ZIQ', '江边村': 'JBG',
    '峨眉': 'EMW', '兰州西': 'LAJ', '昆明': 'KMM', '合肥': 'HFH', '张家口南': 'ZMP', '库车': 'KCR', '太原北': 'TBV', '北安': 'BAB',
    '格尔木': 'GRO', '萍乡': 'PXG'}

TICKET_DATE = "leftTicketDTO.train_date"
TICKET_FROM = "leftTicketDTO.from_station"
TICKET_TO = "leftTicketDTO.to_station"
TICKET_PURPOSE = "purpose_codes"



