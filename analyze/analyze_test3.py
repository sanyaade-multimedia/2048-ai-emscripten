from pylab import *
import numpy

analyze_value = array([
	100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900,
	4100, 4300, 4500, 4700, 4900, 5100, 5300, 5500, 5700, 5900, 6100, 6300, 6500, 6700, 6900, 7100, 7300, 7500, 7700, 7900,
	8100, 8300, 8500, 8700, 8900, 9100, 9300, 9500, 9700, 9900, 10100, 10300, 10500, 10700, 10900, 11100, 11300, 11500, 11700, 11900,
	12100, 12300, 12500, 12700, 12900, 13100, 13300, 13500, 13700, 13900, 14100, 14300, 14500, 14700, 14900, 15100, 15300, 15500, 15700, 15900,
	16100, 16300, 16500, 16700, 16900, 17100, 17300, 17500, 17700, 17900, 18100, 18300, 18500, 18700, 18900, 19100, 19300, 19500, 19700, 19900,
	20100, 20300, 20500, 20700, 20900, 21100, 21300, 21500, 21700, 21900, 22100, 22300, 22500, 22700, 22900, 23100, 23300, 23500, 23700, 23900,
	24100, 24300, 24500])
analyze_score = array([
	[92849, 92569, 92173, 77540], [91560, 91698, 91975, 94415], [90185, 90127, 90090, 89128], [88401, 88411, 88572, 89067], [86997, 87085, 87122, 87465],
	[84840, 85027, 85530, 87199], [82870, 82859, 82793, 82859], [81486, 81481, 81497, 82002], [79808, 79857, 79920, 80080], [78429, 78414, 78411, 78330],
	[76018, 76070, 76306, 75645], [73211, 73218, 73254, 73133], [71941, 71938, 71983, 72473], [70263, 70311, 70394, 70344], [68882, 68821, 68743, 68760],
	[67457, 67433, 67164, 66166], [65705, 65713, 65478, 64553], [64563, 64514, 64333, 63317], [63277, 63183, 62687, 60167], [62475, 62273, 61489, 56248],
	[61534, 61422, 61058, 58496], [58055, 57723, 56785, 51386], [57291, 57211, 57150, 57094], [55878, 55835, 55812, 55479], [54456, 54509, 54681, 55527],
	[53075, 53050, 53057, 52778], [51061, 51052, 50985, 50751], [49757, 49712, 49567, 49106], [48414, 48328, 48012, 46197], [47382, 47172, 46564, 44268],
	[46870, 46682, 46194, 42391], [45503, 45352, 44861, 42274], [45187, 45124, 44962, 44212], [44014, 43866, 43311, 39750], [42852, 42761, 42247, 38479],
	[41904, 41769, 41342, 37410], [41580, 41383, 40700, 36820], [41417, 41275, 40798, 37389], [41143, 40913, 40330, 37610], [41453, 41010, 40196, 35468],
	[43968, 43276, 42087, 38720], [44592, 44637, 44160, 38861], [42754, 42727, 42425, 38271], [41903, 41992, 42086, 41361], [40335, 40336, 40422, 41072],
	[38951, 38929, 38787, 37708], [37341, 37350, 37281, 36824], [35647, 35601, 35533, 35043], [34312, 34300, 34204, 33418], [32983, 32940, 32677, 31533],
	[31906, 31703, 31097, 28047], [30480, 30455, 30356, 29133], [28942, 28905, 28762, 28260], [27909, 27798, 27602, 26606], [26278, 26242, 26111, 25111],
	[25174, 25086, 24685, 22032], [24121, 23999, 23723, 21636], [23304, 23141, 22609, 19242], [22508, 22439, 22058, 19291], [21982, 21783, 21189, 18013],
	[22199, 21811, 21179, 18094], [23639, 23420, 22965, 21343], [22382, 22245, 21646, 17324], [22099, 22070, 21899, 20653], [20814, 20776, 20668, 19752],
	[19500, 19400, 18991, 16332], [18343, 18293, 18128, 16865], [16756, 16758, 16598, 14587], [15787, 15749, 15669, 14397], [14832, 14775, 14538, 13782],
	[14280, 14072, 13627, 12019], [14802, 14543, 14087, 13030], [13506, 13535, 13301, 11326], [13048, 13038, 12797, 11854], [12153, 12084, 11931, 10746],
	[11222, 11293, 11407, 11334], [10945, 10757, 10582, 9795], [11309, 11261, 10696, 8558], [10892, 10809, 10848, 9290], [11637, 11291, 10508, 7567],
	[15393, 14975, 13746, 8226], [29265, 28381, 27124, 29017], [37422, 37947, 39817, 32189], [32272, 31316, 29683, 18662], [32973, 33200, 33497, 34287],
	[31522, 32110, 33347, 36331], [29806, 30088, 30084, 29021], [27787, 27844, 27301, 26785], [25691, 25826, 26471, 26705], [24244, 24012, 23439, 22761],
	[23484, 23466, 23196, 21701], [22015, 22190, 22552, 23235], [19264, 19239, 18842, 14195], [17677, 17541, 16979, 14489], [17476, 17459, 17524, 17103],
	[16691, 16372, 15900, 14077], [15462, 15743, 15533, 13434], [14930, 14861, 15078, 14615], [13835, 13896, 13424, 10243], [12377, 12587, 12923, 5838],
	[13096, 13105, 13194, 11173], [13830, 13666, 12978, 9155], [18376, 18036, 18832, 20371], [20672, 20180, 18850, 10404], [23083, 23131, 23257, 28242],
	[21189, 20772, 19609, 14489], [19834, 19712, 18708, 14829], [18078, 17646, 16859, 12092], [15243, 15106, 13877, 7851], [14074, 13874, 13431, 11959],
	[12484, 12024, 11493, 9313], [10907, 10985, 10343, 7042], [11478, 11116, 10148, 6636], [8949, 8673, 7745, 4234], [11853, 11854, 11618, 4757],
	[10300, 10221, 9939, 8474], [8694, 8643, 8759, 8347], [7423, 7437, 7196, 7758], [4576, 4518, 4523, 3693], [3131, 2975, 2706, 2205],
	[2550, 2667, 2737, 904], [1921, 1908, 1832, 1401], [576, 775, 1001, 1064]])

analyze_value = array([
	100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900,
	4100, 4300, 4500, 4700, 4900, 5100, 5300, 5500, 5700, 5900, 6100, 6300, 6500, 6700, 6900, 7100, 7300, 7500, 7700, 7900,
	8100, 8300, 8500, 8700, 8900, 9100, 9300, 9500, 9700, 9900, 10100, 10300, 10500, 10700, 10900, 11100, 11300, 11500, 11700, 11900,
	12100, 12300, 12500, 12700, 12900, 13100, 13300, 13500, 13700, 13900, 14100, 14300, 14500, 14700, 14900, 15100, 15300, 15500, 15700, 15900,
	16100, 16300, 16500, 16700, 16900, 17100, 17300, 17500, 17700, 17900, 18100, 18300, 18500, 18700, 18900, 19100, 19300, 19500, 19700, 19900,
	20100, 20300, 20500, 20700, 20900, 21100, 21300, 21500, 21700, 21900, 22100, 22300, 22500, 22700, 22900, 23100, 23300, 23500, 23700, 23900,
	24100, 24300, 24500])
analyze_score = array([
	[92849, 91839, 91452, 0], [91560, 92224, 92865, 105080], [90185, 90003, 89713, 89278], [88401, 88609, 88645, 88726], [86997, 87224, 87915, 90966],
	[84840, 85835, 86546, 87676], [82870, 82743, 82934, 82537], [81486, 81513, 81378, 81693], [79808, 80019, 80041, 79913], [78429, 78484, 78496, 78660],
	[76018, 76314, 76504, 75895], [73211, 73263, 73430, 70837], [71941, 71928, 72227, 74134], [70263, 70411, 70449, 69603], [68882, 68732, 68814, 67996],
	[67457, 67051, 66567, 64919], [65705, 65434, 64779, 62922], [64563, 64168, 63110, 63085], [63277, 62530, 61441, 60095], [62475, 61057, 56847, 53799],
	[61534, 60859, 59972, 57914], [58055, 56695, 53733, 50175], [57291, 57164, 56888, 53994], [55878, 55855, 55766, 55031], [54456, 54916, 55526, 56295],
	[53075, 53042, 52783, 52375], [51061, 50841, 50757, 49923], [49757, 49330, 49155, 48967], [48414, 47891, 46710, 44456], [47382, 46345, 44721, 45782],
	[46870, 46070, 44576, 41904], [45503, 44473, 41912, 39083], [45187, 45047, 44574, 41246], [44014, 42998, 41310, 38593], [42852, 41956, 39628, 36598],
	[41904, 41186, 38267, 27983], [41580, 40215, 37769, 35820], [41417, 40519, 38427, 32952], [41143, 39971, 37843, 34085], [41453, 39739, 36428, 22067],
	[43968, 41337, 37062, 30517], [44592, 44568, 44083, 40777], [42754, 42298, 39955, 30308], [41903, 42096, 41784, 38035], [40335, 40490, 40827, 40854],
	[38951, 38744, 37995, 35337], [37341, 37315, 37189, 36837], [35647, 35385, 35261, 35905], [34312, 34161, 33663, 33989], [32983, 32494, 31843, 31051],
	[31906, 30790, 28529, 25814], [30480, 30384, 29875, 28835], [28942, 28733, 28258, 25253], [27909, 27523, 27430, 28054], [26278, 25981, 24985, 24241],
	[25174, 24471, 22758, 18236], [24121, 23563, 22411, 20392], [23304, 22423, 20042, 16246], [22508, 21868, 19217, 12807], [21982, 20883, 18863, 15348],
	[22199, 20994, 18524, 11792], [23639, 22959, 22425, 19936], [22382, 21469, 18497, 11829], [22099, 21742, 20716, 15379], [20814, 20629, 20525, 19658],
	[19500, 18772, 16692, 16630], [18343, 18000, 17503, 15201], [16756, 16486, 14512, 12720], [15787, 15560, 14366, 13715], [14832, 14501, 13893, 13467],
	[14280, 13293, 12097, 7427], [14802, 14168, 13883, 13647], [13506, 13079, 11636, 9352], [13048, 12642, 12338, 10518], [12153, 11721, 11135, 9996],
	[11222, 11350, 11116, 11653], [10945, 10474, 10245, 8189], [11309, 10246, 8560, 6171], [10892, 10609, 9643, 5191], [11637, 9615, 7696, 7798],
	[15393, 13568, 8406, 398], [29265, 27898, 29517, 11961], [37422, 40418, 40835, 35169], [32272, 29316, 21946, 7111], [32973, 33260, 33050, 24998],
	[31522, 33174, 33599, 26579], [29806, 30337, 28892, 25294], [27787, 27256, 27353, 29539], [25691, 26552, 26622, 27297], [24244, 23178, 22943, 22545],
	[23484, 23166, 22337, 20502], [22015, 22675, 24069, 28982], [19264, 18949, 17169, 14221], [17677, 16959, 14569, 8440], [17476, 17685, 17166, 14454],
	[16691, 15204, 13917, 13816], [15462, 15353, 16284, 7446], [14930, 14939, 13332, 10048], [13835, 13069, 9845, 4321], [12377, 11957, 10820, 0],
	[13096, 14006, 10315, 6320], [13830, 12718, 10714, 9931], [18376, 18420, 19665, 15148], [20672, 18921, 12375, 1283], [23083, 23634, 28709, 30528],
	[21189, 19066, 19026, 0], [19834, 18878, 12894, 11968], [18078, 16547, 15005, 11247], [15243, 12869, 10847, 7873], [14074, 13178, 12698, 11428],
	[12484, 11516, 8596, 5358], [10907, 9778, 6990, 14057], [11478, 10613, 7456, 2117], [8949, 6657, 2846, 644], [11853, 11456, 10088, 2],
	[10300, 9679, 9457, 8851], [8694, 8585, 7273, 0], [7423, 7528, 7034, 5567], [4576, 4349, 3432, 4819], [3131, 2722, 2586, 0],
	[2550, 2814, 841, 0], [1921, 1850, 1324, 0], [576, 961, 1015, 0]])

close("all")
figure("Speed2048 - analyze test3", figsize=(16,9))

plot(analyze_value, analyze_score, label="score")
legend(loc="upper right")
xlabel("Board value")
ylabel("Score")
grid()

tight_layout()
show()