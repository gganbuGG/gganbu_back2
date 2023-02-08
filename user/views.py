from rest_framework import viewsets,permissions,generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
import time
import requests
import urllib.parse
from bs4 import BeautifulSoup as bs
from .models import user,match,static
from .serializers import userSerializer,matchSerializer,statSerializer
from django.db.models import Q



class UserAPI(APIView):
    def get(self,request,sname):
        s_name=''
        for i in sname:
            if i!=' ':
                s_name+=i
        users=user.objects.filter(Q(name__iexact=s_name))
        serializer=userSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

def getAPIkey():
    f=open("C:/devrent/back2/user/riot_api.txt","r")
    return f.read()

def pet_K(name):
    pet={13010: '비트메이커 오시아', 13011: '비트메이커 오시아', 13012: '비트메이커 오시아', 13019: '용 춤꾼 오시아', 13020: '용 춤꾼 오시아', 13021: '용 춤꾼 오시아', 13001: '오시아', 13002: '오시아', 13003: '오시아', 13007: '팝의 여왕 오시아', 13008: '팝의 여왕 오시아', 13009: '팝의 여왕 오시아', 13013: '천재 오시아', 13014: '천재 오시아', 13015: '천재 오시아', 13016: '신난 오시아', 13017: '신난 오시아', 13018: '신난 오시아', 13004: '독주자 오시아', 13005: '독주자 오시아', 13006: '독주자 오시아', 25001: '아오 신', 25002: '아오 신', 25003: '아오 신', 25010: '암흑의 별 아오 신', 25011: '암흑의 별 아오 신', 25012: '암흑의 별 아오 신', 25013: '신성한 아오 신', 25014: '신성한 아오 신', 25015: '신성한 아오 신', 25004: '장로 아오 신', 25005: '장로 아오 신', 25006: '장로 아오 신', 25007: '불꽃놀이 아오 신', 25008: '불꽃놀이 아오 신', 25009: '불꽃놀이 아오 신', 25019: '하늘빛 붓꼬리 아오 신', 25020: '하늘빛 붓꼬리 아오 신', 25021: '하늘빛 붓꼬리 아오 신', 25022: '돌풍의 화신 붓꼬리 아오 신', 25023: '돌풍의 화신 붓꼬리 아오 신', 25024: '돌풍의 화신 붓꼬리 아오 신', 25025: '잉걸불 붓꼬리 아오 신', 25026: '잉걸불 붓꼬리 아오 신', 25027: '잉걸불 붓꼬리 아오 신', 25028: '검은불꽃 붓꼬리 아오 신', 25029: '검은불꽃 붓꼬리 아오 신', 25030: '검은불꽃 붓꼬리 아오 신', 25031: '대지 붓꼬리 아오 신', 25032: '대지 붓꼬리 아오 신', 25033: '대지 붓꼬리 아오 신', 25016: '별의 창조자 아오 신', 25017: '별의 창조자 아오 신', 25018: '별의 창조자 아오 신', 25034: '물장구 아오 신', 25035: '물장구 아오 신', 25036: '물장구 아오 신', 39001: '뽀글이', 39002: '뽀글이', 39003: '뽀글이', 39019: '사자춤 뽀글이', 39020: '사자춤 뽀글이', 39021: '사자춤 뽀글이', 39004: '개구리 뽀글이', 39005: '개구리 뽀글이', 39006: '개구리 뽀글이', 39007: '꿀벌 뽀글이', 39008: '꿀벌 뽀글이', 39009: '꿀벌 뽀글이', 39010: '불혀 뽀글이', 39011: '불혀 뽀글이', 39012: '불혀 뽀글이', 39013: '심해 뽀글이', 39014: '심해 뽀글이', 39015: '심해 뽀글이', 39016: '아이스크림 콘 뽀글이', 39017: '아이스크림 콘 뽀글이', 39018: '아이스크림 콘 뽀글이', 51003: '남작이', 51006: '슈퍼특공대 남작이', 51009: '오디세이 남작이', 51012: '별 수호자 남작이', 51015: '별의 숙적 남작이', 51018: '우주의 무법자 남작이', 24013: '검은 안개 방울이', 24014: '검은 안개 방울이', 24015: '검은 안개 방울이', 24016: '핏빛달 방울이', 24017: '핏빛달 방울이', 24018: '핏빛달 방울이', 24001: '방울이', 24002: '방울이', 24003: '방울이', 24019: '도자기 방울이', 24020: '도자기 방울이', 24021: '도자기 방울이', 24007: '달콤 가득 방울이', 24008: '달콤 가득 방울이', 24009: '달콤 가득 방울이', 24004: '천둥 번개 방울이', 24005: '천둥 번개 방울이', 24006: '천둥 번개 방울이', 24010: '성탄절 방울이', 24011: '성탄절 방울이', 24012: '성탄절 방울이', 17016: '꿀벌 총총이', 17017: '꿀벌 총총이', 17018: '꿀벌 총총이', 17001: '총총이', 17002: '총총이', 17003: '총총이', 17013: '이쉬탈 총총이', 17014: '이쉬탈 총총이', 17015: '이쉬탈 총총이', 17010: '군단 총총이', 17011: '군단 총총이', 17012: '군단 총총이', 17007: '모래몰이 총총이', 17008: '모래몰이 총총이', 17009: '모래몰이 총총이', 17019: '감시자 총총이', 17004: '얼음 정수 총총이', 17005: '얼음 정수 총총이', 17006: '얼음 정수 총총이', 17020: '생일 꽃 케익', 52001: '깡충이', 52002: '깡충이', 52003: '깡충이', 52019: '설맞이 축제 깡충이', 52020: '설맞이 축제 깡충이', 52021: '설맞이 축제 깡충이', 52022: '도자기 깡충이', 52023: '도자기 깡충이', 52024: '도자기 깡충이', 52025: '빨간 토끼 깡충이', 52026: '빨간 토끼 깡충이', 52027: '빨간 토끼 깡충이', 52028: '연꽃 깡충이', 52029: '연꽃 깡충이', 52030: '연꽃 깡충이', 52031: '맛있는 깡충이', 52032: '맛있는 깡충이', 52033: '맛있는 깡충이', 52004: '초코 가득 깡충이', 52005: '초코 가득 깡충이', 52006: '초코 가득 깡충이', 52007: '전투 토끼 깡충이', 52008: '전투 토끼 깡충이', 52009: '전투 토끼 깡충이', 52010: '빨간 모자 깡충이', 52011: '빨간 모자 깡충이', 52012: '빨간 모자 깡충이', 52013: '우주 그루브 깡충이', 52014: '우주 그루브 깡충이', 52015: '우주 그루브 깡충이', 52016: '바나나 깡충이', 52017: '바나나 깡충이', 52018: '바나나 깡충이', 54001: '미니 애니', 54002: '미니 판다 애니', 48001: '미니 애쉬', 48002: '미니 용술사 애쉬', 34001: '미니 에코', 35001: '미니 징크스', 35002: '미니 불꽃놀이 징크스', 45001: '미니 카이사', 45002: '미니 용술사 카이사', 44001: '미니 리 신', 44002: '미니 용술사 리 신', 50001: '미니 럭스', 50002: '미니 별 수호자 럭스', 37001: '미니 바이', 38001: '미니 야스오', 38002: '미니 용술사 야스오', 27004: '아틀란티스 배불뚝이', 27005: '아틀란티스 배불뚝이', 27006: '아틀란티스 배불뚝이', 27001: '배불뚝이', 27002: '배불뚝이', 27003: '배불뚝이', 27007: '바위 배불뚝이', 27008: '바위 배불뚝이', 27009: '바위 배불뚝이', 27010: '불꽃 배불뚝이', 27011: '불꽃 배불뚝이', 27012: '불꽃 배불뚝이', 27016: '꿀벌 배불뚝이', 27017: '꿀벌 배불뚝이', 27018: '꿀벌 배불뚝이', 27022: '새해 야수 배불뚝이', 27023: '새해 야수 배불뚝이', 27024: '새해 야수 배불뚝이', 27019: '설맞이 축제 배불뚝이', 27020: '설맞이 축제 배불뚝이', 27021: '설맞이 축제 배불뚝이', 27034: '현자 배불뚝이', 27035: '현자 배불뚝이', 27036: '현자 배불뚝이', 27013: '판다 배불뚝이', 27014: '판다 배불뚝이', 27015: '판다 배불뚝이', 27025: '어푸푸 마을 배불뚝이', 27026: '어푸푸 마을 배불뚝이', 27027: '어푸푸 마을 배불뚝이', 27028: '안전 요원 배불뚝이', 27029: '안전 요원 배불뚝이', 27030: '안전 요원 배불뚝이', 27031: '구릿빛 배불뚝이', 27032: '구릿빛 배불뚝이', 27033: '구릿빛 배불뚝이', 53001: '수염냥', 53002: '수염냥', 53003: '수염냥', 53004: '별 수호자 수염냥', 53005: '별 수호자 수염냥', 53006: '별 수호자 수염냥', 53007: '슈퍼특공대 수염냥', 53008: '슈퍼특공대 수염냥', 53009: '슈퍼특공대 수염냥', 53010: '꿰맨 수염냥', 53011: '꿰맨 수염냥', 53012: '꿰맨 수염냥', 53013: '별의 숙적 수염냥', 53014: '별의 숙적 수염냥', 53015: '별의 숙적 수염냥', 53016: '암흑의 별 수염냥', 53017: '암흑의 별 수염냥', 53018: '암흑의 별 수염냥', 19016: '우주 징징이', 19017: '우주 징징이', 19018: '우주 징징이', 19007: '행성 파괴자 징징이', 19008: '행성 파괴자 징징이', 19009: '행성 파괴자 징징이', 19010: '새콤달콤 징징이', 19011: '새콤달콤 징징이', 19012: '새콤달콤 징징이', 19019: 'K/DA ALL OUT 징징이', 19020: 'K/DA ALL OUT 징징이', 19021: 'K/DA ALL OUT 징징이', 19022: 'K/DA POP/STARS 징징이', 19023: 'K/DA POP/STARS 징징이', 19024: 'K/DA POP/STARS 징징이', 19004: '오디세이 징징이', 19005: '오디세이 징징이', 19006: '오디세이 징징이', 19001: '징징이', 19002: '징징이', 19003: '징징이', 19013: '아이스크림 콘 징징이', 19014: '아이스크림 콘 징징이', 19015: '아이스크림 콘 징징이', 19025: '선인장 징징이', 19026: '선인장 징징이', 19027: '선인장 징징이', 19028: '하이 눈 징징이', 19029: '하이 눈 징징이', 19030: '하이 눈 징징이', 19031: '질서의 징징이', 19032: '질서의 징징이', 19033: '질서의 징징이', 19034: '옥수수 징징이', 19035: '옥수수 징징이', 19036: '옥수수 징징이', 19037: '무법자 징징이', 19038: '무법자 징징이', 19039: '무법자 징징이', 20001: '어둠전사', 20002: '어둠전사', 20003: '어둠전사', 20013: '석회석 어둠전사', 20014: '석회석 어둠전사', 20015: '석회석 어둠전사', 20016: '우주 어둠전사', 20017: '우주 어둠전사', 20018: '우주 어둠전사', 20019: '프로젝트: 어둠전사', 20020: '프로젝트: 어둠전사', 20021: '프로젝트: 어둠전사', 20004: '다르킨 어둠전사', 20005: '다르킨 어둠전사', 20006: '다르킨 어둠전사', 20007: '은하계 학살자 어둠전사', 20008: '은하계 학살자 어둠전사', 20009: '은하계 학살자 어둠전사', 20010: '나무껍질 어둠전사', 20011: '나무껍질 어둠전사', 20012: '나무껍질 어둠전사', 21016: '우주 별고래', 21017: '우주 별고래', 21018: '우주 별고래', 21004: '행성 파괴자 별고래', 21005: '행성 파괴자 별고래', 21006: '행성 파괴자 별고래', 21007: '은하계 학살자 별고래', 21008: '은하계 학살자 별고래', 21009: '은하계 학살자 별고래', 21010: '액체괴물 별고래', 21011: '액체괴물 별고래', 21012: '액체괴물 별고래', 21019: '비단잉어왕 별고래 ', 21020: '비단잉어왕 별고래 ', 21021: '비단잉어왕 별고래 ', 21013: '악마 별고래', 21014: '악마 별고래', 21015: '악마 별고래', 21001: '별고래', 21002: '별고래', 21003: '별고래', 29001: '퐁당이', 29002: '퐁당이', 29003: '퐁당이', 29022: '도자기 퐁당이', 29023: '도자기 퐁당이', 29024: '도자기 퐁당이', 29025: '운수 대통 퐁당이', 29026: '운수 대통 퐁당이', 29027: '운수 대통 퐁당이', 29028: '행운의 국수 퐁당이', 29029: '행운의 국수 퐁당이', 29030: '행운의 국수 퐁당이', 29031: '불닭 퐁당이', 29032: '불닭 퐁당이', 29033: '불닭 퐁당이', 29034: '달콤한 꽃잎 퐁당이', 29035: '달콤한 꽃잎 퐁당이', 29036: '달콤한 꽃잎 퐁당이', 29019: 'U.R.F. 퐁당이', 29020: 'U.R.F. 퐁당이', 29021: 'U.R.F. 퐁당이', 29004: '비단인어 퐁당이', 29005: '비단인어 퐁당이', 29006: '비단인어 퐁당이', 29007: '젤리 퐁당이', 29008: '젤리 퐁당이', 29009: '젤리 퐁당이', 29010: '와플 퐁당이', 29011: '와플 퐁당이', 29012: '와플 퐁당이', 29013: '무지갯빛 퐁당이', 29014: '무지갯빛 퐁당이', 29015: '무지갯빛 퐁당이', 29016: '어둠의 인도자 퐁당이', 29017: '어둠의 인도자 퐁당이', 29018: '어둠의 인도자 퐁당이', 42001: '꽥꽥이', 42002: '꽥꽥이', 42003: '꽥꽥이', 42025: '흥겨운 꽥꽥이', 42026: '흥겨운 꽥꽥이', 42027: '흥겨운 꽥꽥이', 42028: '수룡 꽥꽥이', 42029: '수룡 꽥꽥이', 42030: '수룡 꽥꽥이', 42031: '달빛 학자 꽥꽥이', 42032: '달빛 학자 꽥꽥이', 42033: '달빛 학자 꽥꽥이', 42034: '불꽃놀이 꽥꽥이', 42035: '불꽃놀이 꽥꽥이', 42036: '불꽃놀이 꽥꽥이', 42037: '말썽꾸러기 꽥꽥이', 42038: '말썽꾸러기 꽥꽥이', 42039: '말썽꾸러기 꽥꽥이', 42004: '꿀벌 꽥꽥이', 42005: '꿀벌 꽥꽥이', 42006: '꿀벌 꽥꽥이', 42007: '배달의 기수 꽥꽥이', 42008: '배달의 기수 꽥꽥이', 42009: '배달의 기수 꽥꽥이', 42010: '파자마 파티 꽥꽥이', 42011: '파자마 파티 꽥꽥이', 42012: '파자마 파티 꽥꽥이', 42013: '아이스크림 콘 꽥꽥이', 42014: '아이스크림 콘 꽥꽥이', 42015: '아이스크림 콘 꽥꽥이', 42016: '자운 꽥꽥이', 42017: '자운 꽥꽥이', 42018: '자운 꽥꽥이', 42019: '필트오버 꽥꽥이', 42020: '필트오버 꽥꽥이', 42021: '필트오버 꽥꽥이', 42022: '최고의 꽥꽥이', 42023: '최고의 꽥꽥이', 42024: '최고의 꽥꽥이', 47001: '용발굽', 47002: '용발굽', 47003: '용발굽', 47004: '비단잉어 용발굽', 47005: '비단잉어 용발굽', 47006: '비단잉어 용발굽', 47007: '분노날개 용발굽', 47008: '분노날개 용발굽', 47009: '분노날개 용발굽', 47010: '비취 용발굽', 47011: '비취 용발굽', 47012: '비취 용발굽', 47013: '어둠강림 용발굽', 47014: '어둠강림 용발굽', 47015: '어둠강림 용발굽', 47016: '만년서리 용발굽', 47017: '만년서리 용발굽', 47018: '만년서리 용발굽', 23016: '파알랑이', 23017: '파알랑이', 23018: '파알랑이', 23001: '팔랑이', 23002: '팔랑이', 23003: '팔랑이', 23013: '불닭 팔랑이', 23014: '불닭 팔랑이', 23015: '불닭 팔랑이', 23007: '인어 팔랑이', 23008: '인어 팔랑이', 23009: '인어 팔랑이', 23022: '사교계 팔랑이', 23023: '사교계 팔랑이', 23024: '사교계 팔랑이', 23004: '장미꽃 팔랑이', 23005: '장미꽃 팔랑이', 23006: '장미꽃 팔랑이', 23020: '환호의 팔랑이', 23010: '흡혈귀 팔랑이', 23011: '흡혈귀 팔랑이', 23012: '흡혈귀 팔랑이', 23019: '승리의 팔랑이', 30001: '으르렁이', 30002: '으르렁이', 30003: '으르렁이', 30019: '탄산 으르렁이', 30020: '탄산 으르렁이', 30021: '탄산 으르렁이', 30022: '제트 엔진 으르렁이', 30023: '제트 엔진 으르렁이', 30024: '제트 엔진 으르렁이', 30025: '마법공학 으르렁이', 30026: '마법공학 으르렁이', 30027: '마법공학 으르렁이', 30028: '펄스 건 으르렁이', 30029: '펄스 건 으르렁이', 30030: '펄스 건 으르렁이', 30031: '현상금 사냥꾼 으르렁이', 30032: '현상금 사냥꾼 으르렁이', 30033: '현상금 사냥꾼 으르렁이', 30004: '슈리마 으르렁이', 30005: '슈리마 으르렁이', 30006: '슈리마 으르렁이', 30007: '황금 으르렁이', 30008: '황금 으르렁이', 30009: '황금 으르렁이', 30010: '천공의 화신 으르렁이', 30011: '천공의 화신 으르렁이', 30012: '천공의 화신 으르렁이', 30013: '어둠의 인도자 으르렁이', 30014: '어둠의 인도자 으르렁이', 30015: '어둠의 인도자 으르렁이', 30016: '칸메이 으르렁이', 30017: '칸메이 으르렁이', 30018: '칸메이 으르렁이', 18010: '검은 안개 돌돌이', 18011: '검은 안개 돌돌이', 18012: '검은 안개 돌돌이', 18001: '돌돌이', 18002: '돌돌이', 18003: '돌돌이', 18016: '마법공학 돌돌이', 18017: '마법공학 돌돌이', 18018: '마법공학 돌돌이', 18013: '군단 돌돌이', 18014: '군단 돌돌이', 18015: '군단 돌돌이', 18007: '모래몰이 돌돌이', 18008: '모래몰이 돌돌이', 18009: '모래몰이 돌돌이', 18019: ' 감시자 돌돌이', 18021: '환호의 돌돌이', 18004: '얼음 정수 돌돌이', 18005: '얼음 정수 돌돌이', 18006: '얼음 정수 돌돌이', 18020: '승리의 돌돌이', 7004: '맹렬한 수호대장', 7005: '맹렬한 수호대장', 7006: '맹렬한 수호대장', 7001: '보석박이 수호대장', 7002: '보석박이 수호대장', 7003: '보석박이 수호대장', 7021: '호랑이띠 해 수호대장', 7022: '호랑이띠 해 수호대장', 7023: '호랑이띠 해 수호대장', 7013: '군림하는 수호대장', 7014: '군림하는 수호대장', 7015: '군림하는 수호대장', 7007: '그늘보석 수호대장', 7008: '그늘보석 수호대장', 7009: '그늘보석 수호대장', 7010: '하늘보석 수호대장', 7011: '하늘보석 수호대장', 7012: '하늘보석 수호대장', 7016: '태양의 자손 수호대장', 7017: '태양의 자손 수호대장', 7018: '태양의 자손 수호대장', 7020: '환호의 수호대장', 7019: '승리의 수호대장', 1016: '그림자 가면 유령이', 1017: '그림자 가면 유령이', 1018: '그림자 가면 유령이', 1007: '달빛 발톱 유령이', 1008: '달빛 발톱 유령이', 1009: '달빛 발톱 유령이', 1004: '불꽃 유령이', 1005: '불꽃 유령이', 1006: '불꽃 유령이', 1020: '환호의 유령이', 1010: '맹독 유령이', 1011: '맹독 유령이', 1012: '맹독 유령이', 1022: '화염의 유령이', 1023: '화염의 유령이', 1024: '화염의 유령이', 1025: '장로 유령이', 1026: '장로 유령이', 1027: '장로 유령이', 1028: '바다의 유령이', 1029: '바다의 유령이', 1030: '바다의 유령이', 1031: '대지의 유령이', 1032: '대지의 유령이', 1033: '대지의 유령이', 1034: '바람의 유령이', 1035: '바람의 유령이', 1036: '바람의 유령이', 1013: '암흑 물질 유령이', 1014: '암흑 물질 유령이', 1015: '암흑 물질 유령이', 1021: '감시자 유령이', 1001: '그림자 군도 유령이', 1002: '그림자 군도 유령이', 1003: '그림자 군도 유령이', 1019: '승리의 유령이', 41001: '말캉이', 41002: '말캉이', 41003: '말캉이', 41025: '복숭아 말캉이', 41026: '복숭아 말캉이', 41027: '복숭아 말캉이', 41028: '새우맛 말캉이', 41029: '새우맛 말캉이', 41030: '새우맛 말캉이', 41031: '따뜻한 수프 말캉이', 41032: '따뜻한 수프 말캉이', 41033: '따뜻한 수프 말캉이', 41034: '도자기 말캉이', 41035: '도자기 말캉이', 41036: '도자기 말캉이', 41037: '황금빛 커스터드 말캉이', 41038: '황금빛 커스터드 말캉이', 41039: '황금빛 커스터드 말캉이', 41004: '꿀벌 말캉이', 41005: '꿀벌 말캉이', 41006: '꿀벌 말캉이', 41007: '마법공학 말캉이', 41008: '마법공학 말캉이', 41009: '마법공학 말캉이', 41010: '불꽃 말캉이', 41011: '불꽃 말캉이', 41012: '불꽃 말캉이', 41013: '아케이드 말캉이', 41014: '아케이드 말캉이', 41015: '아케이드 말캉이', 41016: '아이스크림 콘 말캉이', 41017: '아이스크림 콘 말캉이', 41018: '아이스크림 콘 말캉이', 41019: '팝 그루브 말캉이', 41020: '팝 그루브 말캉이', 41021: '팝 그루브 말캉이', 41022: '피자 냠냠 말캉이', 41023: '피자 냠냠 말캉이', 41024: '피자 냠냠 말캉이', 2001: '데마시아 짹짹이', 2002: '데마시아 짹짹이', 2003: '데마시아 짹짹이', 2016: '길 잃은 짹짹이', 2017: '길 잃은 짹짹이', 2018: '길 잃은 짹짹이', 2004: '눈꽃 버찌 짹짹이', 2005: '눈꽃 버찌 짹짹이', 2006: '눈꽃 버찌 짹짹이', 2013: '열대 짹짹이', 2014: '열대 짹짹이', 2015: '열대 짹짹이', 2010: '장미꽃 짹짹이', 2011: '장미꽃 짹짹이', 2012: '장미꽃 짹짹이', 2023: '바람의 짹짹이', 2024: '바람의 짹짹이', 2025: '바람의 짹짹이', 2026: '화염의 짹짹이', 2027: '화염의 짹짹이', 2028: '화염의 짹짹이', 2029: '바다의 짹짹이', 2030: '바다의 짹짹이', 2031: '바다의 짹짹이', 2032: '대지의 짹짹이', 2033: '대지의 짹짹이', 2034: '대지의 짹짹이', 2035: '장로 짹짹이', 2036: '장로 짹짹이', 2037: '장로 짹짹이', 2019: '별 수호자 짹짹이', 2020: '별 수호자 짹짹이', 2021: '별 수호자 짹짹이', 2022: '승리의 짹짹이', 2007: '새벽빛 짹짹이', 2008: '새벽빛 짹짹이', 2009: '새벽빛 짹짹이', 3016: '툰드라 뿔보', 3017: '툰드라 뿔보', 3018: '툰드라 뿔보', 3007: '나무껍질 뿔보', 3008: '나무껍질 뿔보', 3009: '나무껍질 뿔보', 3013: '아이스크림 콘 뿔보', 3014: '아이스크림 콘 뿔보', 3015: '아이스크림 콘 뿔보', 3020: 'K/DA ALL OUT 뿔보', 3021: 'K/DA ALL OUT 뿔보', 3022: 'K/DA ALL OUT 뿔보', 3023: 'K/DA POP/STARS 뿔보', 3024: 'K/DA POP/STARS 뿔보', 3025: 'K/DA POP/STARS 뿔보', 3026: '새해 야수 뿔보', 3027: '새해 야수 뿔보', 3028: '새해 야수 뿔보', 3029: '설맞이 축제 뿔보', 3030: '설맞이 축제 뿔보', 3031: '설맞이 축제 뿔보', 3010: '사자 기운 뿔보', 3011: '사자 기운 뿔보', 3012: '사자 기운 뿔보', 3001: '이글이글 뿔보', 3002: '이글이글 뿔보', 3003: '이글이글 뿔보', 3019: '승리의 뿔보', 3004: '공허에 물든 뿔보', 3005: '공허에 물든 뿔보', 3006: '공허에 물든 뿔보', 16010: '검은 안개 톡톡이', 16011: '검은 안개 톡톡이', 16012: '검은 안개 톡톡이', 16007: '화학공학 톡톡이', 16008: '화학공학 톡톡이', 16009: '화학공학 톡톡이', 16013: '군단 톡톡이', 16014: '군단 톡톡이', 16015: '군단 톡톡이', 16016: '꽃잎 무희 톡톡이', 16017: '꽃잎 무희 톡톡이', 16018: '꽃잎 무희 톡톡이', 16004: '페트리사이트 톡톡이', 16005: '페트리사이트 톡톡이', 16006: '페트리사이트 톡톡이', 16021: '별 수호자 톡톡이', 16022: '별 수호자 톡톡이', 16023: '별 수호자 톡톡이', 16001: '톡톡이', 16002: '톡톡이', 16003: '톡톡이', 16020: '환호의 톡톡이', 16019: '승리의 톡톡이', 43001: '뿜뿜이', 43002: '뿜뿜이', 43003: '뿜뿜이', 43004: '불혀 뿜뿜이', 43005: '불혀 뿜뿜이', 43006: '불혀 뿜뿜이', 43007: '아이스크림 콘 뿜뿜이', 43008: '아이스크림 콘 뿜뿜이', 43009: '아이스크림 콘 뿜뿜이', 43010: '멋쟁이 뿜뿜이', 43011: '멋쟁이 뿜뿜이', 43012: '멋쟁이 뿜뿜이', 43013: '빛나는 뿜뿜이', 43014: '빛나는 뿜뿜이', 43015: '빛나는 뿜뿜이', 43016: '프로젝트: 뿜뿜이', 43017: '프로젝트: 뿜뿜이', 43018: '프로젝트: 뿜뿜이', 55001: '투덜이', 55002: '투덜이', 55003: '투덜이', 55004: '슈퍼특공대 투덜이', 55005: '슈퍼특공대 투덜이', 55006: '슈퍼특공대 투덜이', 55007: '별 수호자 투덜이', 55008: '별 수호자 투덜이', 55009: '별 수호자 투덜이', 55010: '암흑의 별 투덜이', 55011: '암흑의 별 투덜이', 55012: '암흑의 별 투덜이', 55013: '신바람난 투덜이', 55014: '신바람난 투덜이', 55015: '신바람난 투덜이', 55016: '별의 숙적 투덜이', 55017: '별의 숙적 투덜이', 55018: '별의 숙적 투덜이', 4019: '우주비행사 두더지 광부', 4020: '우주비행사 두더지 광부', 4021: '우주비행사 두더지 광부', 4028: '혼돈의 두더지 광부', 4029: '혼돈의 두더지 광부', 4030: '혼돈의 두더지 광부', 4013: '덤벙대는 두더지 광부', 4014: '덤벙대는 두더지 광부', 4015: '덤벙대는 두더지 광부', 4010: '민물 두더지 광부', 4011: '민물 두더지 광부', 4012: '민물 두더지 광부', 4001: '말랑코 두더지 광부', 4002: '말랑코 두더지 광부', 4003: '말랑코 두더지 광부', 4025: '철갑의 두더지 광부', 4026: '철갑의 두더지 광부', 4027: '철갑의 두더지 광부', 4022: '질서의 두더지 광부', 4023: '질서의 두더지 광부', 4024: '질서의 두더지 광부', 4007: '하늘춤 두더지 광부', 4008: '하늘춤 두더지 광부', 4009: '하늘춤 두더지 광부', 4004: '불꽃 작렬 두더지 광부', 4005: '불꽃 작렬 두더지 광부', 4006: '불꽃 작렬 두더지 광부', 4016: '독성 줄줄 두더지 광부', 4017: '독성 줄줄 두더지 광부', 4018: '독성 줄줄 두더지 광부', 5010: '검은 안개 룬정령', 5011: '검은 안개 룬정령', 5012: '검은 안개 룬정령', 5001: '파수꾼 룬정령', 5002: '파수꾼 룬정령', 5003: '파수꾼 룬정령', 5013: '빙하 룬정령', 5014: '빙하 룬정령', 5015: '빙하 룬정령', 5004: '덩굴 룬정령', 5005: '덩굴 룬정령', 5006: '덩굴 룬정령', 5007: '묘목 룬정령', 5008: '묘목 룬정령', 5009: '묘목 룬정령', 5016: '벚꽃 룬정령', 5017: '벚꽃 룬정령', 5018: '벚꽃 룬정령', 5019: '생일 케이크정령', 31001: '날쌘발', 31002: '날쌘발', 31003: '날쌘발', 31004: '어둠의 인도자 날쌘발', 31005: '어둠의 인도자 날쌘발', 31006: '어둠의 인도자 날쌘발', 31007: '구원받은 자 날쌘발', 31008: '구원받은 자 날쌘발', 31009: '구원받은 자 날쌘발', 31010: '킨코우 날쌘발', 31011: '킨코우 날쌘발', 31012: '킨코우 날쌘발', 31013: '신록의 날쌘발', 31014: '신록의 날쌘발', 31015: '신록의 날쌘발', 31016: '망각의 날쌘발', 31017: '망각의 날쌘발', 31018: '망각의 날쌘발', 22016: '아케이드 번쩍이', 22017: '아케이드 번쩍이', 22018: '아케이드 번쩍이', 22013: '검은 안개 번쩍이', 22014: '검은 안개 번쩍이', 22015: '검은 안개 번쩍이', 22001: '번쩍이', 22002: '번쩍이', 22003: '번쩍이', 22004: '수정 번쩍이', 22005: '수정 번쩍이', 22006: '수정 번쩍이', 22010: '하이 눈 번쩍이', 22011: '하이 눈 번쩍이', 22012: '하이 눈 번쩍이', 22019: 'K/DA ALL OUT 번쩍이', 22020: 'K/DA ALL OUT 번쩍이', 22021: 'K/DA ALL OUT 번쩍이', 22022: 'K/DA POP/STARS 번쩍이', 22023: 'K/DA POP/STARS 번쩍이', 22024: 'K/DA POP/STARS 번쩍이', 22025: '스피드광 번쩍이', 22026: '스피드광 번쩍이', 22027: '스피드광 번쩍이', 22028: '마법공학 번쩍이', 22029: '마법공학 번쩍이', 22030: '마법공학 번쩍이', 22031: '펄스 건 번쩍이', 22032: '펄스 건 번쩍이', 22033: '펄스 건 번쩍이', 22034: '신바람난 번쩍이', 22035: '신바람난 번쩍이', 22036: '신바람난 번쩍이', 22037: '풍선껌 레이서 번쩍이', 22038: '풍선껌 레이서 번쩍이', 22039: '풍선껌 레이서 번쩍이', 22007: '아이스크림 콘 번쩍이', 22008: '아이스크림 콘 번쩍이', 22009: '아이스크림 콘 번쩍이', 6032: '혼돈의 펭구', 6033: '혼돈의 펭구', 6034: '혼돈의 펭구', 6001: '펭구 깃털기사', 6002: '펭구 깃털기사', 6003: '펭구 깃털기사', 6004: '까마귀 군주 깃털기사', 6005: '까마귀 군주 깃털기사', 6006: '까마귀 군주 깃털기사', 6038: 'e스포츠 펭구', 6007: '얼음 정수 깃털기사', 6008: '얼음 정수 깃털기사', 6009: '얼음 정수 깃털기사', 6025: 'K/DA ALL OUT 깃털기사', 6026: 'K/DA ALL OUT 깃털기사', 6027: 'K/DA ALL OUT 깃털기사', 6028: 'K/DA POP/STARS 깃털기사', 6029: 'K/DA POP/STARS 깃털기사', 6030: 'K/DA POP/STARS 깃털기사', 6054: '용 조련사 펭구', 6055: '용 조련사 펭구', 6056: '용 조련사 펭구', 6035: '질서의 펭구', 6036: '질서의 펭구', 6037: '질서의 펭구', 6016: '벚꽃 깃털기사', 6017: '벚꽃 깃털기사', 6018: '벚꽃 깃털기사', 6010: '불닭 깃털기사', 6011: '불닭 깃털기사', 6012: '불닭 깃털기사', 6031: '몰락한 펭구', 6019: '칸메이 깃털기사', 6020: '칸메이 깃털기사', 6021: '칸메이 깃털기사', 6022: '아카나 깃털기사', 6023: '아카나 깃털기사', 6024: '아카나 깃털기사', 6039: '검은불꽃 붓꼬리 깃털기사', 6040: '검은불꽃 붓꼬리 깃털기사', 6041: '검은불꽃 붓꼬리 깃털기사', 6042: '잉걸불 붓꼬리 깃털기사', 6043: '잉걸불 붓꼬리 깃털기사', 6044: '잉걸불 붓꼬리 깃털기사', 6045: '돌풍의 화신 붓꼬리 깃털기사', 6046: '돌풍의 화신 붓꼬리 깃털기사', 6047: '돌풍의 화신 붓꼬리 깃털기사', 6048: '대지 붓꼬리 깃털기사', 6049: '대지 붓꼬리 깃털기사', 6050: '대지 붓꼬리 깃털기사', 6051: '하늘빛 붓꼬리 깃털기사', 6052: '하늘빛 붓꼬리 깃털기사', 6053: '하늘빛 붓꼬리 깃털기사', 6013: '병아리 깃털기사', 6014: '병아리 깃털기사', 6015: '병아리 깃털기사', 40001: '요롱뇽', 40002: '요롱뇽', 40003: '요롱뇽', 40004: '꿀벌 요롱뇽', 40005: '꿀벌 요롱뇽', 40006: '꿀벌 요롱뇽', 40007: '빛나는 요롱뇽', 40008: '빛나는 요롱뇽', 40009: '빛나는 요롱뇽', 40010: '리오', 40011: '리오', 40012: '리오', 40013: '새콤달콤 요롱뇽', 40014: '새콤달콤 요롱뇽', 40015: '새콤달콤 요롱뇽', 40016: '마법공학 요롱뇽', 40017: '마법공학 요롱뇽', 40018: '마법공학 요롱뇽', 40019: '화학공학 요롱뇽', 40020: '화학공학 요롱뇽', 40021: '화학공학 요롱뇽', 40022: '물방울무늬 요롱뇽', 40023: '물방울무늬 요롱뇽', 40024: '물방울무늬 요롱뇽', 46001: '용멍이', 46002: '용멍이', 46003: '용멍이', 46004: '꿀벌 용멍이', 46005: '꿀벌 용멍이', 46006: '꿀벌 용멍이', 46007: '장미꽃 용멍이', 46008: '장미꽃 용멍이', 46009: '장미꽃 용멍이', 46010: '비취 용멍이', 46011: '비취 용멍이', 46012: '비취 용멍이', 46013: '별 용멍이', 46014: '별 용멍이', 46015: '별 용멍이', 46016: '사랑스러운 용멍이', 46017: '사랑스러운 용멍이', 46018: '사랑스러운 용멍이', 14016: '베이스 여왕 키키', 14017: '베이스 여왕 키키', 14018: '베이스 여왕 키키', 14010: '비트메이커 키키', 14011: '비트메이커 키키', 14012: '비트메이커 키키', 14004: '열정적인 키키', 14005: '열정적인 키키', 14006: '열정적인 키키', 14013: '천재 키키', 14014: '천재 키키', 14015: '천재 키키', 14019: '짜릿짜릿 키키', 14020: '짜릿짜릿 키키', 14021: '짜릿짜릿 키키', 14022: '신바람난 키키', 14023: '신바람난 키키', 14024: '신바람난 키키', 14025: '마법공학 키키', 14026: '마법공학 키키', 14027: '마법공학 키키', 14028: '아케이드 키키', 14029: '아케이드 키키', 14030: '아케이드 키키', 14031: '펄스 건 키키', 14032: '펄스 건 키키', 14033: '펄스 건 키키', 14001: '키키', 14002: '키키', 14003: '키키', 14007: '독주자 키키', 14008: '독주자 키키', 14009: '독주자 키키', 10004: '풍선껌 말랑이', 10005: '풍선껌 말랑이', 10006: '풍선껌 말랑이', 10001: '말랑이', 10002: '말랑이', 10003: '말랑이', 10007: '생강편 말랑이', 10008: '생강편 말랑이', 10009: '생강편 말랑이', 10010: '알사탕 말랑이', 10011: '알사탕 말랑이', 10012: '알사탕 말랑이', 10013: '상큼앵두 말랑이', 10014: '상큼앵두 말랑이', 10015: '상큼앵두 말랑이', 10019: '도자기 말랑이', 10020: '도자기 말랑이', 10021: '도자기 말랑이', 10022: '행운의 등불 말랑이', 10023: '행운의 등불 말랑이', 10024: '행운의 등불 말랑이', 10025: '불꽃놀이 말랑이', 10026: '불꽃놀이 말랑이', 10027: '불꽃놀이 말랑이', 10028: '사자춤 말랑이', 10029: '사자춤 말랑이', 10030: '사자춤 말랑이', 10031: '사나운 말랑이', 10032: '사나운 말랑이', 10033: '사나운 말랑이', 10016: '당분 과충전 말랑이', 10017: '당분 과충전 말랑이', 10018: '당분 과충전 말랑이', 11028: '혼돈의 꿀렁이', 11029: '혼돈의 꿀렁이', 11030: '혼돈의 꿀렁이', 11016: '샛별 꿀렁이', 11017: '샛별 꿀렁이', 11018: '샛별 꿀렁이', 11010: '그늘진 꿀렁이', 11011: '그늘진 꿀렁이', 11012: '그늘진 꿀렁이', 11013: '불꽃놀이 꿀렁이', 11014: '불꽃놀이 꿀렁이', 11015: '불꽃놀이 꿀렁이', 11001: '꿀렁이', 11002: '꿀렁이', 11003: '꿀렁이', 11004: '마지막 소원 꿀렁이', 11005: '마지막 소원 꿀렁이', 11006: '마지막 소원 꿀렁이', 11007: '사랑에 빠진 꿀렁이', 11008: '사랑에 빠진 꿀렁이', 11009: '사랑에 빠진 꿀렁이', 11019: '행운의 꿀렁이', 11020: '행운의 꿀렁이', 11021: '행운의 꿀렁이', 11025: '신록의 꿀렁이', 11026: '신록의 꿀렁이', 11027: '신록의 꿀렁이', 11022: '질서의 꿀렁이', 11023: '질서의 꿀렁이', 11024: '질서의 꿀렁이', 12016: '타락한 라라', 12017: '타락한 라라', 12018: '타락한 라라', 12025: '라라 박사', 12026: '라라 박사', 12027: '라라 박사', 12013: '불꽃놀이 라라', 12014: '불꽃놀이 라라', 12015: '불꽃놀이 라라', 12004: '용감무쌍 라라', 12005: '용감무쌍 라라', 12006: '용감무쌍 라라', 12007: '꼬맹이 라라', 12008: '꼬맹이 라라', 12009: '꼬맹이 라라', 12022: '새해 야수 라라', 12023: '새해 야수 라라', 12024: '새해 야수 라라', 12019: '설맞이 축제 라라', 12020: '설맞이 축제 라라', 12021: '설맞이 축제 라라', 12001: '라라', 12002: '라라', 12003: '라라', 12010: '햇살기운 라라', 12011: '햇살기운 라라', 12012: '햇살기운 라라', 15010: '비트메이커 멜리스마', 15011: '비트메이커 멜리스마', 15012: '비트메이커 멜리스마', 15004: '열정적인 멜리스마', 15005: '열정적인 멜리스마', 15006: '열정적인 멜리스마', 15025: '연꽃 무희 멜리스마', 15026: '연꽃 무희 멜리스마', 15027: '연꽃 무희 멜리스마', 15028: '축제의 불꽃 멜리스마', 15029: '축제의 불꽃 멜리스마', 15030: '축제의 불꽃 멜리스마', 15031: '도자기 멜리스마', 15032: '도자기 멜리스마', 15033: '도자기 멜리스마', 15034: '천상의 비취 멜리스마', 15035: '천상의 비취 멜리스마', 15036: '천상의 비취 멜리스마', 15037: '행운의 토끼 멜리스마', 15038: '행운의 토끼 멜리스마', 15039: '행운의 토끼 멜리스마', 15001: '멜리스마', 15002: '멜리스마', 15003: '멜리스마', 15007: '팝의 여왕 멜리스마', 15008: '팝의 여왕 멜리스마', 15009: '팝의 여왕 멜리스마', 15013: '천재 멜리스마', 15014: '천재 멜리스마', 15015: '천재 멜리스마', 15016: '그림자 비트 멜리스마', 15017: '그림자 비트 멜리스마', 15018: '그림자 비트 멜리스마', 15019: '칸메이 멜리스마', 15020: '칸메이 멜리스마', 15021: '칸메이 멜리스마', 15022: '아카나 멜리스마', 15023: '아카나 멜리스마', 15024: '아카나 멜리스마', 9016: '영원한 살랑꼬리', 9017: '영원한 살랑꼬리', 9018: '영원한 살랑꼬리', 9004: '요정 살랑꼬리', 9005: '요정 살랑꼬리', 9006: '요정 살랑꼬리', 9025: 'K/DA ALL OUT 살랑꼬리', 9026: 'K/DA ALL OUT 살랑꼬리', 9027: 'K/DA ALL OUT 살랑꼬리', 9028: 'K/DA POP/STARS 살랑꼬리', 9029: 'K/DA POP/STARS 살랑꼬리', 9030: 'K/DA POP/STARS 살랑꼬리', 9010: '이슬송이 살랑꼬리', 9011: '이슬송이 살랑꼬리', 9012: '이슬송이 살랑꼬리', 9007: '제왕 살랑꼬리', 9008: '제왕 살랑꼬리', 9009: '제왕 살랑꼬리', 9001: '달빛 살랑꼬리', 9002: '달빛 살랑꼬리', 9003: '달빛 살랑꼬리', 9019: '칸메이 살랑꼬리', 9020: '칸메이 살랑꼬리', 9021: '칸메이 살랑꼬리', 9022: '아카나 살랑꼬리', 9023: '아카나 살랑꼬리', 9024: '아카나 살랑꼬리', 9013: '야생 살랑꼬리', 9014: '야생 살랑꼬리', 9015: '야생 살랑꼬리', 15: '아케인 도깨비', 6: '혼돈의 도깨비', 1: '강도깨비', 17: '알 도깨비', 18: '사우나 도깨비', 5: '만두 도깨비', 14: '질서의 도깨비', 16: '식물 친구 도깨비', 4: '비취 황제 도깨비', 3: '별 수호자 도깨비', 19: '슈퍼특공대 도깨비', 2: 'UFO 도깨비', 8007: '화산호 첨벙둥이', 8008: '화산호 첨벙둥이', 8009: '화산호 첨벙둥이', 8004: '화려한 첨벙둥이', 8005: '화려한 첨벙둥이', 8006: '화려한 첨벙둥이', 8001: '비취 첨벙둥이', 8002: '비취 첨벙둥이', 8003: '비취 첨벙둥이', 8013: '장미꽃 첨벙둥이', 8014: '장미꽃 첨벙둥이', 8015: '장미꽃 첨벙둥이', 8019: '하늘빛 붓꼬리 첨벙둥이', 8020: '하늘빛 붓꼬리 첨벙둥이', 8021: '하늘빛 붓꼬리 첨벙둥이', 8022: '대지 붓꼬리 첨벙둥이', 8023: '대지 붓꼬리 첨벙둥이', 8024: '대지 붓꼬리 첨벙둥이', 8025: '잉걸불 붓꼬리 첨벙둥이', 8026: '잉걸불 붓꼬리 첨벙둥이', 8027: '잉걸불 붓꼬리 첨벙둥이', 8028: '검은불꽃 붓꼬리 첨벙둥이', 8029: '검은불꽃 붓꼬리 첨벙둥이', 8030: '검은불꽃 붓꼬리 첨벙둥이', 8031: '돌풍의 화신 붓꼬리 첨벙둥이', 8032: '돌풍의 화신 붓꼬리 첨벙둥이', 8033: '돌풍의 화신 붓꼬리 첨벙둥이', 8010: '파도샘 첨벙둥이', 8011: '파도샘 첨벙둥이', 8012: '파도샘 첨벙둥이', 8016: '성탄절 첨벙둥이', 8017: '성탄절 첨벙둥이', 8018: '성탄절 첨벙둥이', 26004: '검은 안개 크릉이', 26005: '검은 안개 크릉이', 26006: '검은 안개 크릉이', 26013: '핏빛달 크릉이', 26014: '핏빛달 크릉이', 26015: '핏빛달 크릉이', 26025: '혼돈의 크릉이', 26026: '혼돈의 크릉이', 26027: '혼돈의 크릉이', 26001: '크릉이', 26002: '크릉이', 26003: '크릉이', 26007: '새콤달콤 크릉이', 26008: '새콤달콤 크릉이', 26009: '새콤달콤 크릉이', 26016: '황금 크릉이', 26017: '황금 크릉이', 26018: '황금 크릉이', 26022: '용족 크릉이', 26023: '용족 크릉이', 26024: '용족 크릉이', 26019: '질서의 크릉이', 26020: '질서의 크릉이', 26021: '질서의 크릉이', 26028: '작은 상어 크릉이', 26029: '작은 상어 크릉이', 26030: '작은 상어 크릉이', 26031: '안전 요원 크릉이', 26032: '안전 요원 크릉이', 26033: '안전 요원 크릉이', 26034: '과일 스무디 크릉이', 26035: '과일 스무디 크릉이', 26036: '과일 스무디 크릉이', 26037: '구릿빛 크릉이', 26038: '구릿빛 크릉이', 26039: '구릿빛 크릉이', 26040: '스쿠버 상어 크릉이 ', 26041: '스쿠버 상어 크릉이 ', 26042: '스쿠버 상어 크릉이 ', 26010: '천둥괴물 크릉이', 26011: '천둥괴물 크릉이', 26012: '천둥괴물 크릉이'}
    return pet[name]


def Item_K(name):
    item = {
    'TFT_Consumable_NeekosHelp': '챔피언 복제기',
    'TFT_Item_BFSword': 'B.F. 대검', 
    'TFT_Item_Bloodthirster': '피바라기', 
    'TFT_Item_BrambleVest': '덤불 조끼', 
    'TFT_Item_ChainVest': '쇠사슬 조끼', 
    'TFT_Item_SparringGloves': '연습용 장갑',
    'TFT_Item_Deathblade': '죽음의 검',
    'TFT_Item_DragonsClaw': '용의 발톱', 
    'TFT_Item_EmptyBag': '',
    'TFT_Item_ForceOfNature': '전략가의 왕관',
    'TFT_Item_ThiefsGloves': '도적의 장갑',
    'TFT_Item_ThiefsGloves_Empty': '', 
    'TFT_Item_Shroud': '침묵의 장막',
    'TFT_Item_FrozenHeart': '수호자의 맹세', 
    'TFT_Item_GiantsBelt': '거인의 허리띠', 
    'TFT_Item_MadredsBloodrazor': '거인 학살자', 
    'TFT_Item_GuardianAngel': '밤의 끝자락', 
    'TFT_Item_GuinsoosRageblade': '구인수의 격노검',
    'TFT_Item_UnstableConcoction': '정의의 손길', 
    'TFT_Item_HextechGunblade': '마법공학 총검', 
    'TFT_Item_Chalice': '힘의 성배', 
    'TFT_Item_InfinityEdge': '무한의 대검', 
    'TFT_Item_IonicSpark': '이온 충격기',
    'TFT_Item_JeweledGauntlet': '보석 건틀릿', 
    'TFT_Item_LastWhisper': '최후의 속삭임',
    'TFT_Item_LocketOfTheIronSolari': '강철의 솔라리 펜던트',
    'TFT_Item_ArchangelsStaff': '대천사의 지팡이',
    'TFT_Item_Spatula': '뒤집개', 
    'TFT_Item_Quicksilver': '수은', 
    'TFT_Item_Morellonomicon': '모렐로노미콘',
    'TFT_Item_NeedlesslyLargeRod': '쓸데없이 큰 지팡이', 
    'TFT_Item_NegatronCloak': '음전자 망토',
    'TFT_Item_PowerGauntlet': '방패파괴자', 
    'TFT_Item_RabadonsDeathcap': '라바돈의 죽음모자', 
    'TFT_Item_RapidFireCannon': '고속 연사포', 
    'TFT_Item_RecurveBow': '곡궁', 
    'TFT_Item_RedBuff': '태양불꽃 망토', 
    'TFT_Item_Redemption': '구원',
    'TFT_Item_RunaansHurricane': '루난의 허리케인', 
    'TFT_Item_SeraphsEmbrace': '푸른 파수꾼',
    'TFT_Item_SpearOfShojin': '쇼진의 창', 
    'TFT_Item_StatikkShiv': '스태틱의 단검',
    'TFT_Item_GargoyleStoneplate': '가고일 돌갑옷',
    'TFT_Item_TearOfTheGoddess': '여신의 눈물',
    'TFT_Item_TitanicHydra': '즈롯 차원문',
    'TFT_Item_TitansResolve': '거인의 결의',
    'TFT_Item_WarmogsArmor': '워모그의 갑옷',
    'TFT_Item_ZekesHerald': '지크의 전령',
    'TFT_Item_Zephyr': '서풍', 
    'TFT_Consumable_ItemRemover': '자석 제거기',
    'TFT_Consumable_ItemReroller': '재조합기', 
    'TFT_Consumable_ShopReroller': '사기 주사위', 
    'TFT4_Item_OrnnAnimaVisage': '영혼의 형상',
    'TFT4_Item_OrnnDeathsDefiance': '죽음의 저항', 
    'TFT4_Item_OrnnEternalWinter': '영원한 겨울',
    'TFT4_Item_OrnnTheCollector': '황금 징수의 총', 
    'TFT4_Item_OrnnInfinityForce': '무한한 삼위일체',
    'TFT4_Item_OrnnMuramana': '마나자네', 
    'TFT4_Item_OrnnObsidianCleaver': '흑요석 양날 도끼',
    'TFT4_Item_OrnnRanduinsSanctum': '란두인의 성소', 
    'TFT4_Item_OrnnRocketPropelledFist': '로켓 주먹', 
    'TFT4_Item_OrnnZhonyasParadox': '존야의 역설',
    'TFT5_Item_TrapClawRadiant': '의지파괴자',
    'TFT5_Item_BloodthirsterRadiant': '축복받은 피바라기',
    'TFT5_Item_BlueBuffRadiant': '푸른 축복',
    'TFT5_Item_ChaliceOfPowerRadiant': '선의의 성배', 
    'TFT5_Item_IonicSparkRadiant': '집단 충격기', 
    'TFT5_Item_GiantSlayerRadiant': '악마 학살자',
    'TFT5_Item_DragonsClawRadiant': '용의 의지',
    'TFT5_Item_GargoyleStoneplateRadiant': '수호상 돌갑옷',
    'TFT5_Item_LastWhisperRadiant': '영겁의 속삭임',
    'TFT5_Item_HandOfJusticeRadiant': '공정의 주먹',
    'TFT5_Item_FrozenHeartRadiant': '철갑의 서약',
    'TFT5_Item_JeweledGauntletRadiant': '눈부신 건틀릿', 
    'TFT5_Item_GuardianAngelRadiant': '새벽의 서광',
    'TFT5_Item_GuinsoosRagebladeRadiant': '구인수의 심판', 
    'TFT5_Item_HextechGunbladeRadiant': '마법공학 생명검',
    'TFT5_Item_LocketOfTheIronSolariRadiant': '타곤 정상의 펜던트', 
    'TFT5_Item_DeathbladeRadiant': '빛나는 죽음의 검', 
    'TFT5_Item_ZephyrRadiant': '겨울바람',
    'TFT5_Item_MorellonomiconRadiant': '엔젤로노미콘', 
    'TFT5_Item_QuicksilverRadiant': '반짝이는 수은', 
    'TFT5_Item_RabadonsDeathcapRadiant': '라바돈의 초월한 죽음모자',
    'TFT5_Item_RedemptionRadiant': '면죄', 
    'TFT5_Item_RapidFirecannonRadiant': '고속 광자포',
    'TFT5_Item_ThiefsGlovesRadiant': '장난꾸러기의 장갑',
    'TFT5_Item_BrambleVestRadiant': '장미가시 조끼',
    'TFT5_Item_RunaansHurricaneRadiant': '루난의 폭풍', 
    'TFT5_Item_ShroudOfStillnessRadiant': '경외의 장막',
    'TFT5_Item_SpearOfShojinRadiant': '히라나의 창', 
    'TFT5_Item_StatikkShivRadiant': '스태틱의 호의',
    'TFT5_Item_SunfireCapeRadiant': '태양빛 망토',
    'TFT5_Item_TitansResolveRadiant': '거인의 맹세',
    'TFT5_Item_ArchangelsStaffRadiant': '우르프 천사의 지팡이',
    'TFT5_Item_WarmogsArmorRadiant': '워모그의 자부심',
    'TFT5_Item_ZekesHeraldRadiant': '지크의 조화', 
    'TFT5_Item_InfinityEdgeRadiant': '천공의 대검',
    'TFT5_Item_ZzRotPortalRadiant': '즈롯 소환문', 
    'TFT7_Item_ShimmerscaleDeterminedInvestor': '결단력 있는 투자자',
    'TFT7_Item_ShimmerscaleDravensAxe': '드레이븐의 도끼', 
    'TFT7_Item_ShimmerscaleMogulsMail': '거물의 갑옷',
    'TFT7_Item_ShimmerscaleGamblersBlade': '도박꾼의 칼날',
    'TFT7_Item_ShimmerscaleHeartOfGold': '쓸데없이 큰 보석', 
    'TFT7_Item_ShimmerscaleGoldmancersStaff': '황금술사의 지팡이', 
    'TFT7_Item_ShimmerscaleDiamondHands': '다이아몬드 손',
    'TFT8_Item_AnimaSquadEmblemItem': '동물특공대 상징',
    'TFT8_Item_CivilianEmblemItem': '민간인 상징', 
    'TFT8_Item_StarGuardianEmblemItem': '별 수호자 상징',
    'TFT8_Item_InterPolarisEmblemItem': '레이저단 상징', 
    'TFT8_Item_OxForceEmblemItem': '황소부대 상징', 
    'TFT8_Item_UndergroundTheEmblemItem': '지하세계 상징',
    'TFT8_Item_GenAEEmblemItem': '기계유망주 상징', 
    'TFT8_Item_ADMINEmblemItem': '자동방어체계 문장',
    'TFT8_Item_MascotEmblemItem': '마스코트 상징',
    'TFT8_Item_DefenderEmblemItem': '엄호대 상징',
    'TFT8_Item_ReconEmblemItem': '정찰단 상징',
    'TFT8_Item_RenegadeEmblemItem': '무법자 상징',
    'TFT8_Item_BrawlerEmblemItem': '싸움꾼 상징', 
    'TFT8_Item_HackerEmblemItem': '해커 상징', 
    'TFT8_Item_DuelistEmblemItem': '결투가 상징',
    'TFT8_Item_HeartEmblemItem': '선의 상징',
    'TFT8_Item_PranksterEmblemItem': '익살꾼 상징',
    'TFT8_Item_DeadeyeEmblemItem': '특등사수 상징',
    'TFT8_Item_GiantSlayer_GenAE': '과부하_ 오류 // 거인 학살자 ',
    'TFT8_Item_HandOfJustice_GenAE': '비결정적 정의의 손길',
    'TFT8_Item_RapidFireCannon_GenAE': '용수철이 든 고속 연사포',
    'TFT8_Item_Shojin_GenAE': '날뛰는 쇼진의 창',
    'TFT8_Item_Shroud_GenAE': '더 고요한 침묵의 장막',
    'TFT8_Item_Sunfire_GenAE': '과열된 태양불꽃 망토', 
    'TFT8_Item_Warmogs_GenAE': '유도집전형 워모그의 갑옷', 
    'TFT8_Item_ArsenalRedGun': '맹공',
    'TFT8_AdminEffect_Mana': '마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_Item_ArsenalBlueGun': '황혼파',
    'TFT8_AdminCause_OnCast': '', 
    'TFT8_Item_ArsenalPurpleGun': '속박의 월식', 
    'TFT8_AdminCause_CombatStart': '전투 시작: ', 
    'TFT8_AdminCause_EveryXAttacks': '', 
    'TFT8_AdminCause_EveryXSeconds': '', 
    'TFT8_AdminCause_HealthThreshold': '',
    'TFT8_AdminCause_OnEnemyDeath': '',
    'TFT8_AdminEffect_AttackSpeed': '공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminEffect_GainAP': '주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminEffect_Gold': '@TFTUnitProperty.item:TFT8_Admin_GoldChance@% 확률로 골드 획득',
    'TFT8_AdminEffect_Shield': '체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_Item_ExoPrimeEmblemItem': '메카: 프라임 상징',
    'TFT8_Item_AceEmblemItem': '에이스 상징',
    'TFT_Assist_Gold_5': '5골드',
    'TFT_Assist_Gold_6': '6골드',
    'TFT_Assist_Gold_7': '7골드',
    'TFT_Assist_Gold_8': '8골드',
    'TFT_Assist_Gold_10': '10골드',
    'TFT_Assist_Gold_16': '16골드',
    'TFT8_AdminCause_AllyDeath': '',
    'TFT8_AdminEffect_GainAD': '공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminEffect_Heal': '체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminEffect_PermanentHealth': '최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminEffect_SingleTargetDamage': '자동방어체계 유닛의 현재 대상에게 고정 피해를 입히는 미사일 발사',
    'TFT_Assist_Gold_34': '34골드',
    'TFT_Assist_Gold_18': '18골드',
    'TFT_Assist_Gold_22': '22골드', 
    'TFT_Assist_Gold_54': '54골드',
    'TFT_Assist_Gold_12': '12골드',
    'TFT_Assist_Gold_20': '20골드',
    'TFT_Assist_Gold_24': '24골드',
    'TFT_Assist_Gold_36': '36골드',
    'TFT_Assist_Gold_76': '76골드',
    'TFT_Assist_Gold_30': '30골드',
    'TFT_Assist_Gold_25': '25골드',
    'TFT_Assist_Gold_40': '40골드',
    'TFT_Assist_Gold_100': '100골드',
    'TFT_Assist_Gold_26': '26골드',
    'TFT_Assist_Gold_126': '126골드',
    'TFT_Assist_Gold_44': '44골드',
    'TFT_Assist_Gold_64': '64골드',
    'TFT_Assist_Gold_154': '154골드',
    'TFT8_Item_ChannelerEmblemItem': '주문투척자 상징',
    'TFT_Random_5_Cost': '감옥 탈출!',
    'TFT_Random_Two_Star_4_Cost': '감옥 탈출!',
    'TFT8_Consumable_ExoPrime_PrimeMarker': '프라임 선택기',
    'TFT8_Item_AegisEmblemItem': '방패대 상징',
    'TFT8_AdminCauseEffect_AllyDeath_GainAP': '아군 사망 시 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_PermanentHealth': '체력이 40%일 때 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnCast_AttackSpeed': '스킬 사용 시 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_GainMana': '아군 사망 시 자동방어체계 유닛이 마나 @TFTUnitProperty.trait:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_AllyDeath_Shield': '아군 자동방어체계 유닛 사망 시 최대 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_AllyDeath_AttackSpeed': '아군 사망 시 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_Heal': '아군 사망 시 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_AllyDeath_GainAD': '아군 사망 시 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_PermanentHealth': '아군 사망 시 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnCast_GainAP': '스킬 사용 시 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_OnCast_Mana': '스킬 사용 시 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_OnCast_Shield': '스킬 사용 시 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_OnCast_Heal': '스킬 사용 시 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_OnCast_GainAD': '스킬 사용 시 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_GainAP': '3번째 기본 공격을 할 때마다 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_Mana': '3번째 기본 공격을 할 때마다 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_AdminCauseEffect_EveryXAttacks_Shield': '3번째 기본 공격을 할 때마다 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_AttackSpeed': '3번째 기본 공격을 할 때마다 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_Heal': '3번째 기본 공격을 할 때마다 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXAttacks_GainAD': '3번째 기본 공격을 할 때마다 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_PermanentHealth': '3번째 기본 공격을 할 때마다 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnKill_GainAP': '처치 시 처치자가 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_OnKill_Mana': '처치 시 처치자가 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_AdminCauseEffect_OnKill_Shield': '처치 시 처치자가 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득', 
    'TFT8_AdminCauseEffect_OnKill_AttackSpeed': '처치 시 처치자가 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득', 
    'TFT8_AdminCauseEffect_OnKill_Heal': '처치 시 처치자가 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_OnKill_GainAD': '처치 시 처치자가 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득', 
    'TFT8_AdminCauseEffect_OnKill_PermanentHealth': '처치 시 처치자가 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득', 
    'TFT8_AdminCauseEffect_HealthThreshold_GainAP': '체력이 40%일 때 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Mana': '체력이 40%일 때 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Shield': '체력이 40%일 때 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_AttackSpeed': '체력이 40%일 때 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Heal': '체력이 40%일 때 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_HealthThreshold_GainAD': '체력이 40%일 때 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_GainAP': '전투 시작: 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStart_Mana': '전투 시작: 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStart_Shield': '전투 시작: 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_CombatStart_AttackSpeed': '전투 시작: 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_GainAD': '전투 시작: 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_PermanentHealth': '전투 시작: 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_GainAP': '5초마다 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Mana': '5초마다 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Shield': '5초마다 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_AttackSpeed': '5초마다 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Heal': '5초마다 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXSeconds_GainAD': '5초마다 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_PermanentHealth': '5초마다 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_Item_Bloodthirster_GenAE': '톱날 피바라기',
    'TFT8_AdminCauseEffect_OnCast_PermanentHealth': '스킬 사용 시 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_Item_IonicSpark_GenAE': '자화 이온 충격기', 'TFT8_AdminCause_CombatStartTeam': '전투 시작: ',
    'TFT8_AdminCause_EveryXSecondsTeam': '전투 시작: ',
    'TFT8_AdminCauseEffect_CombatStartTeam_AttackSpeed': '전투 시작: 아군이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_GainAD': '전투 시작: 아군이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_GainAP': '전투 시작: 아군이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_Mana': '전투 시작: 아군이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_PermHP': '전투 시작: 아군이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_Shield': '전투 시작: 아군이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_AttackSpeed': '5초마다 아군이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_GainAD': '5초마다 아군이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_GainAP': '5초마다 아군이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_Heal': '5초마다 아군이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_Mana': '5초마다 아군이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_PermHP': '5초마다 아군이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT_Item_GrantCompletedAnvil': '완성 아이템 열쇠',
    'TFT_Item_GrantComponentAnvil': '조합 아이템 열쇠',
    'TFT_Item_GrantTomeOfTraits': '특성의 고서', 
    'TFT_Item_GrantCompletedItem1': '완성 아이템 1개',
    'TFT_Item_GrantCompletedItem2': '완성 아이템 @ItemsToGive@개',
    'TFT_Item_GrantCompletedItem3': '완성 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent1': '조합 아이템 1개',
    'TFT_Item_GrantComponent2': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent3': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent4': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent5': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent6': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent7': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent8': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent9': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantOrbs1': '전리품 구 1개',
    'TFT_Item_GrantOrnnAnvil': '오른의 아이템 모루'
    }

    return item[name]

def champ_K(name):
    champ = {
    "TFT8_Kaisa" : "카이사",
    "TFT8_Lux" : "럭스",
    "TFT8_Kayle" : "케일",
    "TFT8_Poppy" : "뽀삐",
    "TFT8_Galio" : "갈리오",
    "TFT8_Rell" : "렐",
    "TFT8_Velkoz" : "벨코즈",
    "TFT8_Nilah" : "닐라",
    "TFT8_Ashe" : "애쉬",
    "TFT8_Yasuo" : "야스오",
    "TFT8_Senna" : "세나",
    "TFT8_Zed" : "제드",
    "TFT8_Lulu" : "룰루",
    "TFT8_Nunu" : "누누",
    "TFT8_Yuumi" : "유미",
    "TFT8_Zoe" : "조이",
    "TFT8_Taliyah" : "탈리야",
    "TFT8_Sivir" : "시비르",
    "TFT8_Gangplank" : "갱플랭크",
    "TFT8_WuKong" : "오공",
    "TFT8_Draven" : "드레이븐",
    "TFT8_Malphite" : "말파이트",
    "TFT8_Nasus" : "나서스",
    "TFT8_Jinx" : "징크스",
    "TFT8_Vayne" : "베인",
    "TFT8_MissFortune" : "미스포츈",
    "TFT8_Chogath" : "초가스",
    "TFT8_Rammus" : "람머스",
    "TFT8_BelVeth" : "벨베스",
    "TFT8_AurelionSol" : "아우렐리온솔",
    "TFT8_Zac" : "자크",
    "TFT8_Mordekaiser" : "모데카이저",
    "TFT8_Leblanc" : "르블랑",
    "TFT8_Sylas" : "사일러스",
    "TFT8_Camille" : "카밀",
    "TFT8_Ezreal" : "이즈리얼",
    "TFT8_Sona" : "소나",
    "TFT8_Ekko" : "에코",
    "TFT8_Sett" : "세트",
    "TFT8_Janna" : "잔나",
    "TFT8_Urgot" : "우르곳",
    "TFT8_Syndra" : "신드라",
    "TFT8_Fiddlesticks" : "피들스틱",
    "TFT8_Blitzcrank" : "블리츠크랭크",
    "TFT8_Renekton" : "레넥톤",
    "TFT8_Vi" : "바이",
    "TFT8_LeeSin" : "리신",
    "TFT8_Riven" : "리븐",
    "TFT8_Jax" : "잭스",
    "TFT8_Sejuani" : "세주아니",
    "TFT8_Soraka" : "소라카",
    "TFT8_Talon" : "탈론",
    "TFT8_Fiora" : "피오라",
    "TFT8_Annie" : "애니",
    "TFT8_Alistar" : "알리스타",
    "TFT8_Viego" : "비에고",
    "TFT8_Samira" : "사미라",
    "TFT8_Aphelios" : "아펠리오스",
    "TFT8_Leona" : "레오나"
    }

    return champ[name]

def Aug_K(name):
    augments = {
    'TFT6_Augment_ForceOfNature': '신병',
    'TFT6_Augment_FirstAidKit': '응급처치 키트 I',
    'TFT6_Augment_MaxLevel10': '레벨 업!', 
    'TFT6_Augment_ItemGrabBag1': '아이템 꾸러미 I', 
    'TFT6_Augment_ItemGrabBag2': '아이템 꾸러미 II', 
    'TFT6_Augment_Windfall': '뜻밖의 횡재',
    'TFT6_Augment_GrandGambler': '큰손',
    'TFT6_Augment_CalculatedLoss': '계산된 패배', 
    'TFT6_Augment_SalvageBin': '재활용 쓰레기통',
    'TFT6_Augment_SlowAndSteady': '진보의 행진',
    'TFT6_Augment_PortableForge': '휴대용 대장간', 
    'TFT6_Augment_HighEndShopping': '품격있는 쇼핑', 
    'TFT6_Augment_Diversify1': '단결된 의지 I', 
    'TFT6_Augment_Diversify2': '단결된 의지 II',
    'TFT6_Augment_Diversify3': '단결된 의지 III',
    'TFT6_Augment_BandOfThieves2': '도둑 무리 II',
    'TFT6_Augment_Featherweights1': '경량급 I',
    'TFT6_Augment_Featherweights2': '경량급 II', 
    'TFT6_Augment_Featherweights3': '경량급 III',
    'TFT6_Augment_HyperRoll': '수완가',
    'TFT6_Augment_MetabolicAccelerator': '대사 촉진제',
    'TFT6_Augment_MakeshiftArmor1': '임시변통 방어구 I',
    'TFT6_Augment_MakeshiftArmor2': '임시변통 방어구 II',
    'TFT6_Augment_Ascension': '초월', 
    'TFT6_Augment_BinaryAirdrop': '이중 공중 보급',
    'TFT6_Augment_ClearMind': '맑은 정신',
    'TFT6_Augment_ThriftShop': '현명한 소비', 
    'TFT6_Augment_Recombobulator': '대격변 생성기', 
    'TFT6_Augment_RadiantRelics': '찬란한 유물',
    'TFT6_Augment_JeweledLotus': '보석 연꽃',
    'TFT6_Augment_VerdantVeil': '신록의 장막',
    'TFT6_Augment_TinyTitans': '꼬마 거인', 
    'TFT6_Augment_ComponentGrabBag': '재료 꾸러미', 
    'TFT6_Augment_Twins2': '문제가 두 배 II', 
    'TFT6_Augment_Twins3': '문제가 두 배 III',
    'TFT6_Augment_FuturePeepers2': '예견 II',
    'TFT6_Augment_TrueTwos': '곱빼기',
    'TFT6_Augment_TriForce1': '3에 깃든 힘 I',
    'TFT6_Augment_TriForce2': '3에 깃든 힘 II',
    'TFT6_Augment_TriForce3': '3에 깃든 힘 III',
    'TFT6_Augment_TheGoldenEgg': '황금 알', 
    'TFT7_Augment_ThinkFast': '빠른 판단',
    'TFT7_Augment_Bloodlust1': '전투 훈련',
    'TFT7_Augment_SacrificialPact': '잔혹한 계약',
    'TFT7_Augment_PandorasBench': '판도라의 대기석',
    'TFT7_Augment_AxiomArc2': '원칙의 원형낫 II',
    'TFT7_Augment_ClutteredMind': '어수선한 마음',
    'TFT6_Augment_TradeSector': '교환의 장',
    'TFT6_Augment_Distancing': '추방자 I', 
    'TFT6_Augment_Distancing2': '추방자 II',
    'TFT6_Augment_ThreesCompany': '삼총사',
    'TFT7_Augment_UrfsGrabBag2': '우르프의 꾸러미 II',
    'TFT7_Augment_LivingForge': '간이 대장간',
    'TFT7_Augment_AFK': '자리 비움',
    'TFT7_Augment_BandOfThieves1': '도둑 무리 I',
    'TFT7_Augment_LategameSpecialist': '후반 전문가',
    'TFT7_Augment_Preparation': '준비 I',
    'TFT7_Augment_BigFriend': '커다란 친구 I',
    'TFT7_Augment_LastStand': '최후의 저항',
    'TFT6_Augment_TargetDummies': '허수아비 전선',
    'TFT7_Augment_CursedCrown': '저주받은 왕관',
    'TFT6_Augment_CyberneticImplants1': '사이버네틱 이식술 I',
    'TFT6_Augment_CelestialBlessing1': '천상의 축복 I',
    'TFT6_Augment_SecondWind1': '재생의 바람 I',
    'TFT6_Augment_CyberneticShell1': '사이버네틱 외피 I',
    'TFT6_Augment_CyberneticUplink1': '사이버네틱 통신 I',
    'TFT6_Augment_CyberneticImplants3': '사이버네틱 이식술 III',
    'TFT6_Augment_CyberneticShell3': '사이버네틱 외피 III',
    'TFT6_Augment_CyberneticUplink3': '사이버네틱 통신 III',
    'TFT6_Augment_RichGetRicher': '부익부', 
    'TFT6_Augment_RichGetRicherPlus': '부익부+',
    'TFT6_Augment_Electrocharge1': '고전압 I', 
    'TFT6_Augment_LudensEcho1': '루덴의 메아리 I', 
    'TFT6_Augment_CelestialBlessing2': '천상의 축복 II', 
    'TFT6_Augment_CelestialBlessing3': '천상의 축복 III',
    'TFT6_Augment_SecondWind2': '재생의 바람 II',
    'TFT6_Augment_ThrillOfTheHunt1': '사냥의 전율 I', 
    'TFT6_Augment_ThrillOfTheHunt2': '사냥의 전율 II',
    'TFT6_Augment_LudensEcho2': '루덴의 메아리 II',
    'TFT6_Augment_LudensEcho3': '루덴의 메아리 III', 
    'TFT6_Augment_Electrocharge2': '고전압 II',
    'TFT6_Augment_Electrocharge3': '고전압 III', 
    'TFT6_Augment_CyberneticImplants2': '사이버네틱 이식술 II',
    'TFT6_Augment_CyberneticShell2': '사이버네틱 외피 II',
    'TFT6_Augment_CyberneticUplink2': '사이버네틱 통신 II',
    'TFT6_Augment_SunfireBoard': '태양불꽃판',
    'TFT6_Augment_WindfallPlus': '뜻밖의 횡재+',
    'TFT6_Augment_WindfallPlusPlus': '뜻밖의 횡재++',
    'TFT7_Augment_FirstAidKit2': '응급처치 키트 II',
    'TFT7_Augment_BigFriend2': '커다란 친구 II', 
    'TFT7_Augment_Preparation2': '준비 II', 
    'TFT7_Augment_Preparation3': '준비 III',
    'TFT6_Augment_TradeSectorPlus': '교환의 장+', 
    'TFT8_Augment_ThreatMaxHealth': '위협 레벨: 최대',
    'TFT8_Augment_AceEmblem': '에이스 문장',
    'TFT8_Augment_AceEmblem2': '에이스 왕관', 
    'TFT8_Augment_ADMINEmblem': '자동방어체계 문장',
    'TFT8_Augment_ADMINEmblem2': '자동방어체계 왕관',
    'TFT8_Augment_AnimaSquadEmblem': '동물특공대 문장', 
    'TFT8_Augment_AnimaSquadEmblem2': '동물특공대 왕관',
    'TFT8_Augment_BrawlerEmblem': '싸움꾼 문장', 
    'TFT8_Augment_BrawlerEmblem2': '싸움꾼 왕관',
    'TFT8_Augment_ChannelerEmblem': '주문투척자 문장',
    'TFT8_Augment_ChannelerEmblem2': '주문투척자 왕관',
    'TFT8_Augment_CivilianEmblem': '민간인 문장',
    'TFT8_Augment_CivilianEmblem2': '민간인 왕관',
    'TFT8_Augment_DeadeyeEmblem': '특등사수 문장',
    'TFT8_Augment_DeadeyeEmblem2': '특등사수 왕관',
    'TFT8_Augment_DefenderEmblem': '엄호대 문장',
    'TFT8_Augment_DefenderEmblem2': '엄호대 왕관',
    'TFT8_Augment_DuelistEmblem': '결투가 문장',
    'TFT8_Augment_DuelistEmblem2': '결투가 왕관',
    'TFT8_Augment_ExoPrimeEmblem': '메카: 프라임 문장',
    'TFT8_Augment_ExoPrimeEmblem2': '메카: 프라임 왕관',
    'TFT8_Augment_GenAETrait2': '기계유망주 영혼',
    'TFT8_Augment_AegisEmblem': '방패대 문장',
    'TFT8_Augment_AegisEmblem2': '방패대 왕관', 
    'TFT8_Augment_HackerEmblem': '해커 문장', 
    'TFT8_Augment_HackerEmblem2': '해커 왕관', 
    'TFT8_Augment_HeartEmblem': '선의 문장', 
    'TFT8_Augment_HeartEmblem2': '선의 왕관',
    'TFT8_Augment_InterPolarisEmblem': '레이저단 문장',
    'TFT8_Augment_InterPolarisEmblem2': '레이저단 왕관',
    'TFT8_Augment_MascotEmblem': '마스코트 문장',
    'TFT8_Augment_MascotEmblem2': '마스코트 왕관',
    'TFT8_Augment_OxForceEmblem': '황소부대 문장',
    'TFT8_Augment_OxForceEmblem2': '황소부대 왕관',
    'TFT8_Augment_PranksterEmblem': '익살꾼 문장', 
    'TFT8_Augment_PranksterEmblem2': '익살꾼 왕관',
    'TFT8_Augment_ReconEmblem': '정찰단 문장', 
    'TFT8_Augment_ReconEmblem2': '정찰단 왕관', 
    'TFT8_Augment_RenegadeEmblem': '무법자 문장', 
    'TFT8_Augment_RenegadeEmblem2': '무법자 왕관',
    'TFT8_Augment_StarGuardianEmblem': '별 수호자 문장',
    'TFT8_Augment_StarGuardianEmblem2': '별 수호자 왕관',
    'TFT8_Augment_UndergroundTheTrait2': '지하세계 영혼', 
    'TFT6_Augment_WoodlandCharm': '숲의 부적', 
    'TFT7_Augment_LuckyGloves': '행운의 장갑', 
    'TFT7_Augment_ScopedWeapons1': '조준경 부착 I',
    'TFT6_Augment_Battlemage1': '전투 마법사 I',
    'TFT6_Augment_Battlemage2': '전투 마법사 II',
    'TFT6_Augment_Battlemage3': '전투 마법사 III',
    'TFT6_Augment_MeleeStarBlade1': '나이프의 날 I',
    'TFT6_Augment_MeleeStarBlade2': '나이프의 날 II',
    'TFT6_Augment_MeleeStarBlade3': '나이프의 날 III',
    'TFT7_Augment_BirthdayPresents': '생일 선물', 
    'TFT7_Augment_Consistency': '일관성', 
    'TFT8_Augment_AnimaSquadTrait': '동물특공대 심장',
    'TFT8_Augment_StarGuardianTrait': '별 수호자 심장',
    'TFT8_Augment_InterPolarisTrait': '레이저단 심장',
    'TFT8_Augment_OxForceTrait': '황소부대 심장',
    'TFT8_Augment_GenAETrait': '기계유망주 심장',
    'TFT8_Augment_MascotTrait': '마스코트 심장',
    'TFT8_Augment_DefenderTrait': '엄호대 심장', 
    'TFT8_Augment_ChannelerTrait': '주문투척자 심장', 
    'TFT8_Augment_BrawlerTrait': '싸움꾼 심장', 
    'TFT8_Augment_DuelistTrait': '결투가 심장', 
    'TFT8_Augment_HeartTrait': '선의 심장',
    'TFT8_Augment_DeadeyeTrait': '특등사수 심장', 
    'TFT8_Augment_ReconTrait': '정찰단 심장',
    'TFT8_Augment_RenegadeTrait': '무법자 심장',
    'TFT8_Augment_UndergroundTheTrait': '지하세계 심장',
    'TFT8_Augment_SupersTrait': '우세 심장', 
    'TFT8_Augment_SupersTrait2': '우세 영혼',
    'TFT8_Augment_ADMINTrait': '자동방어체계 심장', 
    'TFT8_Augment_HackerTrait': '해커 심장', 
    'TFT6_Augment_TomeOfTraits1': '고대의 기록 보관소 I',
    'TFT7_Augment_TomeOfTraits2': '고대의 기록 보관소 II', 
    'TFT6_Augment_Traitless2': '다른 태생 II', 
    'TFT6_Augment_Traitless3': '다른 태생 III',
    'TFT6_Augment_FuturePeepers': '예견 I',
    'TFT6_Augment_GachaAddict': '황금 티켓',
    'TFT8_Augment_BelVethVoidmother': '공허 어미',
    'TFT8_Augment_AurelionSolImpact': '충격 속도',
    'TFT8_Augment_ChoGathMR': '우주의 방어막',
    'TFT8_Augment_RammusArmor': '중무장 아르마딜로',
    'TFT8_Augment_VelkozFrostburn': '동상',
    'TFT8_Augment_ZacSupersize': '거대화', 
    'TFT8_Augment_SonaExile': '전력망', 
    'TFT8_Augment_SonaSupport': '암류',
    'TFT8_Augment_AlistarAoEPulverizer': '강타!',
    'TFT8_Augment_JaxASCarry': '가차없는 맹공',
    'TFT8_Augment_SennaASCarry': '면죄', 
    'TFT8_Augment_NilahReflection': '나눔의 미덕',
    'TFT8_Augment_ZoeDoubleTrouble': '이중 방울',
    'TFT8_Augment_SennaSupport': '레이저단 진형',
    'TFT8_Augment_AlistarBeefUp': '괴수',
    'TFT8_Augment_RivenReverberation': '반향',
    'TFT8_Augment_AnnieCarry': '반사 방패', 
    'TFT8_Augment_AnnieSupport': '불타는 영혼',
    'TFT8_Augment_CamilleCarry': '적응형 방어 체계',
    'TFT8_Augment_LeeSinSupport': '고양',
    'TFT8_Augment_RellSupport': '변화의 철마술',
    'TFT8_Augment_YuumiSupport': '슈우우웅!',
    'TFT8_Augment_ViSupport': '권투 교습',
    'TFT8_Augment_SivirSupport': '끝없는 피자',
    'TFT8_Augment_KaisaStarCrossed': '엇갈린 별', 
    'TFT8_Augment_YasuoCarry': '흡수의 바람', 
    'TFT8_Augment_LeBlancGlitch': '조준 보정', 
    'TFT8_Augment_FioraCarry': '전방의 검사', 
    'TFT8_Augment_EzrealSupport': '도굴꾼의 전리품',
    'TFT8_Augment_JinxCarry': '신난다!',
    'TFT8_Augment_MalphiteCarry': '견고',
    'TFT8_Augment_NasusCarry': '쌓고 또 쌓고',
    'TFT8_Augment_DravenCarry': '드레이븐의 리그',
    'TFT8_Augment_KaisaCarry': '다중 사격', 
    'TFT8_Augment_GalioCarry': '정의의 주먹', 
    'TFT8_Augment_GalioSupport': '안전제일',
    'TFT8_Augment_AurelionSolCarry': '대멸종',
    'TFT8_Augment_JaxSupport': '회피',
    'TFT8_Augment_LuxCarry': '눈부신 특이점',
    'TFT8_Augment_PoppyCarry': '더 크고 튼튼한 방패',
    'TFT8_Augment_ApheliosSupport': '발포 준비 완료',
    'TFT8_Augment_LuxSupport': '빛의 방어막',
    'TFT8_Augment_GangplankSupport': '수금', 
    'TFT8_Augment_SylasCarry': '국왕시해자', 
    'TFT8_Augment_SylasSupport': '페트리사이트 사슬',
    'TFT8_Augment_SettCarry': '펀치 프로토콜',
    'TFT8_Augment_KayleCarry': '거룩한 승천', 
    'TFT8_Augment_KayleSupport': '정의로운 사거리',
    'TFT8_Augment_EkkoSupport': '시공간 붕괴', 
    'TFT8_Augment_MordekaiserCarry': '헤비하지 않은 메탈',
    'TFT8_Augment_VelkozSupport': '얼어붙은 땅',
    'TFT8_Augment_SettSupport': '재생형 보호막', 
    'TFT8_Augment_TalonCarry': '검의 군주',
    'TFT8_Augment_MissFortuneCarry': '토끼 용병',
    'TFT8_Augment_ChoGathCarry': '에너지 공허', 
    'TFT8_Augment_SyndraSupport': '예비전력 강화',
    'TFT8_Augment_RammusCarry': '가시박힌 껍질', 
    'TFT8_Augment_LeonaCarry': '완벽한 흑점 폭발', 
    'TFT8_Augment_NunuSupport': '퍼지는 웃음', 
    'TFT8_Augment_FiddlesticksCarry': '끔찍한 기억', 
    'TFT8_Augment_UrgotCarry': '반짝반짝', 
    'TFT8_Augment_JannaSupport': '과장된 보도',
    'TFT8_Augment_SamiraCarry': '스타일과 재능', 
    'TFT8_Augment_TaliyahSupport': '돌처럼 단단하게',
    'TFT8_Augment_ZedSupport': '약자 멸시', 
    'TFT8_Augment_BlitzcrankCarry': '동적 방어', 
    'TFT8_Augment_UrgotSupport': '밀물',
    'TFT8_Augment_BlitzcrankSupport': '로켓 손',
    'TFT8_Augment_MordekaiserSupport': '말살', 
    'TFT8_Augment_ApheliosCarry': '철갑탄', 
    'TFT8_Augment_LuluSupport': '성장 촉진', 
    'TFT8_Augment_LeonaSupport': '절정의 일식',
    'TFT8_Augment_SejuaniCarry': '빙하 감옥',
    'TFT8_Augment_SyndraCarry': '압도적인 힘',
    'TFT8_Augment_WukongSupport': '재충전',
    'TFT8_Augment_AsheCarry': '레이저단 집중',
    'TFT8_Augment_AsheSupport': '레이저단 몰입',
    'TFT8_Augment_NilahSupport': '승리의 장막',
    'TFT8_Augment_VayneSupport': '한밤의 서곡', 
    'TFT8_Augment_RivenSupport': '금의환향',
    'TFT8_Augment_ZoeSupport': '한숨 잘 시간',
    'TFT8_Augment_LeBlancSupport': '거울 환영', 
    'TFT8_Augment_LeeSinCarry': '정화의 방호', 
    'TFT8_Augment_YuumiCarry': '포식자의 정확성',
    'TFT8_Augment_FiddlesticksSupport': '완전한 타락',
    'TFT8_Augment_PoppySupport': '굳건한 태세',
    'TFT8_Augment_JannaCarry': '신속한 보도',
    'TFT8_Augment_RenegadePartners': '공범',
    'TFT8_Augment_TaliyahCarry': '바위술사',
    'TFT8_Augment_ZedCarry': '그림자술',
    'TFT8_Augment_SivirCarry': '배달팁',
    'TFT8_Augment_RenektonCarry': '분노의 지배',
    'TFT8_Augment_ViCarry': '무자비한 힘', 
    'TFT8_Augment_RenektonSupport': '양떼 도륙', 
    'TFT8_Augment_RellCarry': '진형 유지', 
    'TFT8_Augment_FioraSupport': '황소의 활력', 
    'TFT8_Augment_DravenSupport': '무자비한 칼날', 
    'TFT8_Augment_YasuoSupport': '추방자의 기백', 
    'TFT8_Augment_NasusSupport': '영혼의 포식자', 
    'TFT8_Augment_SorakaSupport': '융화', 
    'TFT8_Augment_LuluCarry': '급속 성장',
    'TFT8_Augment_SorakaCarry': '업그레이드: 광란',
    'TFT8_Augment_VayneCarry': '확산 사격', 
    'TFT8_Augment_MalphiteSupport': '수호자 영혼',
    'TFT8_Augment_BelVethCarry': '피의 복수',
    'TFT8_Augment_EkkoCarry': '공진',
    'TFT8_Augment_GangplankCarry': '불타는 도탄',
    'TFT8_Augment_JinxSupport': '전부 터져라!',
    'TFT8_Augment_MissFortuneSupport': '총알은 비를 타고', 
    'TFT8_Augment_CamilleSupport': '마법공학 응징',
    'TFT8_Augment_WukongCarry': '회전격', 
    'TFT8_Augment_SejuaniSupport': '산산조각', 
    'TFT8_Augment_ZacSupport': '새총 발사',
    'TFT8_Augment_NunuCarry': '눈 굴러가요',
    'TFT8_Augment_ViegoCarry': '심장을 멈추는 자',
    'TFT8_Augment_SamiraSupport': '무모한 자',
    'TFT8_Augment_TalonSupport': '황소부대의 분노',
    'TFT8_Augment_EzrealCarry': '끓어오르는 주문의 힘'
    }

    return augments[name]

def trait_K(name):
    traits={
        "Set8_AnimaSquad" : "동물 특공대",
        "Set8_Aegis" : "방패대",
        "Set8_Brawler" : "싸움꾼",
        "Set8_Civilian" : "민간인",
        "Set8_Duelist" :"결투가", 
        "Set8_GenAE":"기계유망주",
        "Set8_Heart" :"선의",
        "Set8_Mascot": "마스코트",
        "Set8_OxForce": "황소부대",
        "Set8_StarGuardian": "별 수호자",
        "Set8_Supers" : "우세",
        "Set8_Ace" : "에이스",
        "Set8_Defender" : "엄호대",
        "Set8_ExoPrime": "메카: 프라임",
        "Set8_SpaceCorps":"레이저단",
        "Set8_Channeler":"주문투척자",
        "Set8_Forecaster":"기상캐스터",
        "Set8_Prankster":"익살꾼",
        "Set8_Recon" :"정찰단",
        "Set8_UndergroundThe":"지하세계",
        "Set8_Deadeye":"특등사수",
        "Set8_Renegade":"무법자",
        "Set8_Corrupted":"타락",
        "Set8_Threat":"위협",
        "Set8_Arsenal":"병기고",
        "Set8_Hacker":"해커",
        "Set8_Admin":"자동방어체계",

    }
    return traits[name]


class usersAPI(APIView):
    def get(self,request,sname):
        s_name=''
        for i in sname:
            if i!=' ':
                s_name+=i
        matches=match.objects.filter(Q(Name__name__iexact=s_name))
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request,sname):
        key=getAPIkey()
        
        summonername=sname
        
        response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}') #데이터 불러오기

        if response.status_code==200: # 정상처리
                print('기다려주세요')
                pass

        elif response.status_code==404:#사용자 이름 못찾음
            if user.objects.filter(name=summonername):
                obj = user.objects.filter(name=summonername)
                obj.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)


        elif response.status_code == 429:
            print('api cost full : infinite loop start')
            start_time = time.time()

            while True: # 429error가 끝날 때까지 무한 루프
                    if response.status_code == 429:
                        print('try 10 second wait time')
                        time.sleep(10)
                        url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}'
                        response = requests.get(url)
                        print(response.status_code)

                    elif response.status_code == 200: #다시 response 200이면 loop escape
                        print('total wait time : ', time.time() - start_time)                            
                        print('recovery api cost')
                        break

        elif response.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
                    print('service available error')
                    start_time = time.time()

                    while True:
                        if response.status_code == 503 or response.status_code == 429:

                            print('try 10 second wait time')
                            time.sleep(10)
                            url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}'
                            response = requests.get(url)
                            print(response.status_code)

                        elif response.status_code == 200: # 똑같이 response가 정상이면 loop escape
                            print('total error wait time : ', time.time() - start_time)
                            print('recovery api cost')
                            break

        elif response.status_code == 403: # api갱신이 필요
                print('you need api renewal')
                print('break')

        data=response.json()
        name=''
        for i in data["name"]:
            if i!=' ':
                name+=i
        
        puuid=data['puuid']
        level=data['summonerLevel']
        
        u=user(name=name,Puuid=puuid,Level=level)# 유저 테이블에 puuid 와 이름, level저장
        if u in user.objects.all():
            obj = user.objects.filter(name=name)
            obj.delete()
        u.save()

        
        #match id 가져오기
        response_match=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={key}')
        ids=response_match.json() #match id들 가져오기
        
        #foreign key
        s_name=user.objects.filter(Puuid=puuid)
        name=s_name[0]


        # 티어 LP 크롤링
        croll=''
        for i in range(0,len(sname)): # 공백제거
            if sname[i]!=' ':
                croll+=sname[i]
        encode = urllib.parse.quote_plus(croll)
        a=requests.get("https://lolchess.gg/profile/kr/"+encode)
        req=a.text
        soup=bs(req,'html.parser')
        #더블업모드 티어 및 LP
        b=soup.find_all('div','tier-ranked-info__content')[1]
        if b.find('strong'):
            tier=b.find('strong').text
            tier=str(tier).strip()
            LP=b.find('span').text
            LP=LP[:-2]

        else:
            tier=b.find('span').text
            LP=0



        # 통계 모델 만들기
        stat=static(Name=name,Level=level,Tier=tier,LP=LP)
        if stat in static.objects.all():
            obj = static.objects.filter(Name=name)
            obj.delete()
        stat.save()
        


        

        #match 정보 가져오기
        for matchid in ids:
            response=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')

            if response.status_code==200:
                pass
            elif response.status_code==429:
                print('대기시간이 초과되었습니다. 잠시 기다려주세요')
                start_time = time.time()

                while True: # 429error가 끝날 때까지 무한 루프
                        if response.status_code == 429:
                            print('try 10 second wait time')
                            time.sleep(10)
                            response=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')
                            print(response.status_code)

                        elif response.status_code == 200: #다시 response 200이면 loop escape
                            print('total wait time : ', time.time() - start_time)
                            print('recovery api cost')
                            break
            elif response.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
                    print('service available error')
                    

            elif response.status_code == 403: # api갱신이 필요
                print('you need api renewal')
                print('break')
                    

            data = response.json()
            rank=0
            petID=''
            game_level=0
            traits={}
            augments=[]
            units=[]
            
            
            if data["info"]['tft_game_type'] == 'pairs':
                m = match.objects.filter(Matchid = matchid)
                if not m :
                    for i in range(len(data["metadata"]["participants"])):
                        if data["metadata"]["participants"][i] in user.objects.all():
                            obj=user.objects.filter(Puuid=data["metadata"]["participants"][i])
                            data["metadata"]["participants"][i]=obj["Name"]
                        else:
                            PUUID=data["metadata"]["participants"][i]
                            response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{PUUID}?api_key={key}')
                            if response.status_code==200:
                                
                                namedata=response.json()
                                nickname=''
                                for p in namedata["name"]:
                                    if p!=' ':
                                        nickname+=p
                                playerpuuid=namedata['puuid']
                                level=namedata['summonerLevel']
                                u=user(name=nickname,Puuid=playerpuuid,Level=level)# 유저 테이블에 puuid 와 이름, level저장
                                u.save()
                                data["metadata"]["participants"][i]=nickname
                            elif response.status_code==429:
                                print('대기시간이 초과되었습니다. 잠시 기다려주세요')
                                start_time = time.time()

                                while True: # 429error가 끝날 때까지 무한 루프
                                        if response.status_code == 429:
                                            print('try 10 second wait time')
                                            time.sleep(10)
                                            response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{PUUID}?api_key={key}')
                                            print(response.status_code)

                                        elif response.status_code == 200: #다시 response 200이면 loop escape
                                            namedata=response.json()
                                            nickname=''
                                            for p in namedata["name"]:
                                                if p!=' ':
                                                    nickname+=p
                                            playerpuuid=namedata['puuid']
                                            level=namedata['summonerLevel']
                                            u=user(name=nickname,Puuid=playerpuuid,Level=level)# 유저 테이블에 puuid 와 이름, level저장
                                            u.save()
                                            data["metadata"]["participants"][i]=nickname
                                            break

                    participant1=data["metadata"]["participants"][0]
                    participant2=data["metadata"]["participants"][1]
                    participant3=data["metadata"]["participants"][2]
                    participant4=data["metadata"]["participants"][3]
                    participant5=data["metadata"]["participants"][4]
                    participant6=data["metadata"]["participants"][5]
                    participant7=data["metadata"]["participants"][6]
                    participant8=data["metadata"]["participants"][7]
                    
                    for i in data["info"]['participants']:
                        if puuid == i["puuid"]:
                            if i['placement']<3:
                                rank=1
                            elif i['placement']<5:
                                rank=2
                            elif i['placement']<7:
                                rank=3
                            else:
                                rank=4
                            petID=pet_K(i["companion"]['item_ID'])
                            game_level=i['level']
                            #활성화되어있는 특성만 뽑기
                            for j in i["traits"]:
                                if j["tier_current"]>=1:
                                    traits[trait_K(j["name"])]=j["num_units"]
                            
                            for j in i["augments"]:
                                augments.append(Aug_K(j))
                                
                            for j in i["units"]:
                                dict={}
                                dict["Champion"]=champ_K(j["character_id"])
                                item=[]
                                for k in j["itemNames"]:
                                    item.append(Item_K(k))
                                dict["items"]=item
                                dict["rarity"]=j["rarity"]
                                dict["tier"]=j["tier"]
                                units.append(dict)
                                

                    s=static.objects.get(Name=name)
                    s.Total_game+=1
                    s.sum_of_rank+=rank
                    if rank==1:
                        s.Win+=1
                        s.Top2+=1
                    elif rank==2:
                        s.Top2+=1
                    s.save()

                    mat=match(Name=name,Matchid=matchid,Rank=rank,PetID=petID,Game_level=game_level,Traits=traits,Augments=augments,Units=units,Participant1=participant1,Participant2=participant2,Participant3=participant3,Participant4=participant4,Participant5=participant5,Participant6=participant6,Participant7=participant7,Participant8=participant8)
                    mat.save()

                    
        
        matches=match.objects.filter(Name=name)
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class statAPI(APIView):
    def get(self,request,sname):
        
        stat=static.objects.filter(Name=sname)
        serializer=statSerializer(stat,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

