function setFormEnabled(a) {
    $("#calc-osago select").prop("disabled", !a), $("#btn-calc").prop("disabled", a)
}
function setProgress(a) {
    $("#progress").css("width", a + "%").attr("data-label", "Заполнено " + a + "% информации.")
}
function updateItogRows() {
    $("#pricep_row:visible").length > 0 ? $("#itog_pricep").removeClass("closed") : $("#itog_pricep").addClass("closed"), $("#moshnost_row:visible").length > 0 ? $("#itog_moshnost").removeClass("closed") : $("#itog_moshnost").addClass("closed"), 1 == usl_val ? $("#itog_region").addClass("closed") : $("#itog_region").removeClass("closed"), isJur && 0 == usl_val || $("#period_fl_row:visible").length > 0 || $("#period_ul_row:visible").length > 0 ? $("#itog_period").removeClass("closed") : $("#itog_period").addClass("closed"), 2 == usl_val ? $("#itog_ogranicheniya").addClass("closed") : $("#itog_ogranicheniya").removeClass("closed"), $("#spisok_row:visible").length > 0 && 1 == $("#spisok").val() || 2 == usl_val && !isJur ? $("#itog_voditeli").removeClass("closed") : $("#itog_voditeli").addClass("closed"), $("#klass_row:visible").length > 0 ? $("#itog_kbm").removeClass("closed") : $("#itog_kbm").addClass("closed"), $("#narush_row:visible").length > 0 ? $("#itog_narusheniya").removeClass("closed") : $("#itog_narusheniya").addClass("closed")
}
function resetVals(a) {
    for (var b = 0; b < a.length; b++)"jur" == a[b] ? ($("#vladelec").val(-1), $("#vladelec_clear").addClass("closed")) : "uslovie" == a[b] ? ($("#usloviya").val(-1), $("#usloviya_ur").val(-1), $("#usloviya_clear").addClass("closed")) : "tip-ts" == a[b] ? ($("#tip-ts").val(-1), $("#tip-ts_clear").addClass("closed")) : "moshnost" == a[b] ? ($("#moshnost").val(-1), $("#moshnost_clear").addClass("closed")) : "pricep" == a[b] ? ($("#pricep").val(-1), $("#pricep_clear").addClass("closed")) : "region" == a[b] ? ($("#region").val(-1), $("#city_row").addClass("closed"), $("#region_clear").addClass("closed")) : "city" == a[b] ? ($('select[name*="city-"]').val(-1), $("#city_clear").addClass("closed")) : "period" == a[b] ? ($("#period-fl").val(-1), $("#period-ul").val(-1), $("#period-in").val(-1), $("#period-fl_clear").addClass("closed"), $("#period-ul_clear").addClass("closed"), $("#period-in_clear").addClass("closed")) : "spisok" == a[b] ? ($("#spisok").val(-1), $("#spisok_clear").addClass("closed")) : "voditeli" == a[b] ? ($("#voditeli").val(-1), $("#voditeli_clear").addClass("closed")) : "klass" == a[b] ? ($("#Kbm").val(-1), $("#Kbm_clear").addClass("closed")) : "narush" == a[b] && ($("#narusheniya").val(-1), $("#narusheniya_clear").addClass("closed"))
}
function setJur(a) {
    isJur = a, $("#vladelec").prop("disabled", !0), $("#vladelec_clear").removeClass("closed"), setProgress(10), isJur ? ($("#usloviya").addClass("closed"), $("#usloviya_ur").removeClass("closed"), $("#usl_row").removeClass("closed"), $("#usloviya_ur").focus()) : ($("#usloviya").removeClass("closed"), $("#usloviya_ur").addClass("closed"), $("#usl_row").removeClass("closed"), $("#usloviya").focus()), resetVals(["uslovie"])
}
function uslovieChanged(a) {
    usl_val = a, $("#usloviya").prop("disabled", !0), $("#usloviya_ur").prop("disabled", !0), $("#usloviya_clear").removeClass("closed"), setProgress(20), resetVals(["tip-ts"]), $("#tip_ts_row").removeClass("closed"), $("#tip-ts").focus()
}
function tipTSChanged(a) {
    $("#tip-ts").prop("disabled", !0), $("#tip-ts_clear").removeClass("closed"), setProgress(30), resetVals(["moshnost", "pricep"]), "b" == a || "b-t" == a ? ($("#moshnost_row").removeClass("closed"), $("#moshnost").focus()) : ($("#pricep_row").removeClass("closed"), $("#pricep").focus())
}
function moshnostChanged(a) {
    $("#moshnost").prop("disabled", !0), $("#moshnost_clear").removeClass("closed"), resetVals(["region", "period", "spisok"]), setProgress(40), isJur ? ($("#pricep_row").removeClass("closed"), $("#pricep").focus()) : 1 == usl_val ? ($("#spisok_row").removeClass("closed"), $("#spisok").focus(), setProgress(50)) : 2 == usl_val ? ($("#period_in_row").removeClass("closed"), $("#period-in").focus(), setProgress(50)) : ($("#region_row").removeClass("closed"), $("#region").focus())
}
function pricepChanged(a) {
    $("#pricep").prop("disabled", !0), $("#pricep_clear").removeClass("closed"), resetVals(["region", "spisok", "period"]), setProgress(50), 1 == usl_val ? isJur ? ($("#btn-calc").prop("disabled", !1), setProgress(100)) : ($("#spisok_row").removeClass("closed"), $("#spisok").focus(), setProgress(50)) : 2 == usl_val ? ($("#period_in_row").removeClass("closed"), $("#period-in").focus(), setProgress(50)) : ($("#region_row").removeClass("closed"), $("#region").focus())
}
function regionChanged(a) {
    $("#region").prop("disabled", !0), $('select[name*="city-"]').addClass("closed"), $("#region_clear").removeClass("closed"), resetVals(["city", "period", "spisok", "klass"]);
    var b = $("#city-" + a);
    setProgress(60), b.length > 0 ? (b.removeClass("closed"), $("#city_row").removeClass("closed"), b.focus()) : ($("#city_row").addClass("closed"), 2 == usl_val ? ($("#period_in_row").removeClass("closed"), $("#period-in").focus()) : 1 == usl_val ? isJur ? ($("#btn-calc").prop("disabled", !1), setProgress(100)) : ($("#spisok_row").removeClass("closed"), $("#spisok").focus()) : isJur ? (3 == usl_val ? ($("#period_ul_row").removeClass("closed"), $("#period-ul").focus()) : ($("#period_ul_row").addClass("closed"), $("#klass_row").removeClass("closed"), $("#Kbm").focus()), $("#period_fl_row").addClass("closed"), $("#period_in_row").addClass("closed")) : ($("#period_fl_row").removeClass("closed"), $("#period-fl").focus(), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed")))
}
function cityChanged(a) {
    $('select[name*="city-"]').prop("disabled", !0), $("#city_clear").removeClass("closed"), resetVals(["period", "spisok", "klass"]), setProgress(65), 2 == usl_val ? $("#period_in_row").removeClass("closed") : 1 == usl_val ? isJur ? ($("#btn-calc").prop("disabled", !1), setProgress(100)) : ($("#spisok_row").removeClass("closed"), $("#spisok").focus()) : isJur ? (3 == usl_val ? ($("#period_ul_row").removeClass("closed"), $("#period-ul").focus()) : ($("#period_ul_row").addClass("closed"), $("#klass_row").removeClass("closed"), $("#Kbm").focus()), $("#period_fl_row").addClass("closed"), $("#period_in_row").addClass("closed")) : ($("#period_fl_row").removeClass("closed"), $("#period-fl").focus(), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"))
}
function periodChanged(a) {
    $("#period-fl").prop("disabled", !0), $("#period-ul").prop("disabled", !0), $("#period-in").prop("disabled", !0), $("#period-fl_clear").removeClass("closed"), $("#period-ul_clear").removeClass("closed"), $("#period-in_clear").removeClass("closed"), resetVals(["spisok", "narush"]), setProgress(70), 2 == usl_val ? ($("#narush_row").removeClass("closed"), $("#narusheniya").focus(), setProgress(75)) : isJur ? ($("#klass_row").removeClass("closed"), $("#Kbm").focus()) : ($("#spisok_row").removeClass("closed"), $("#spisok").focus())
}
function spisokChanged(a) {
    $("#spisok").prop("disabled", !0), $("#spisok_clear").removeClass("closed"), resetVals(["voditeli", "klass"]), 1 == a ? ($("#voditeli_row").removeClass("closed"), $("#voditeli").focus(), setProgress(80)) : 1 == usl_val ? ($("#btn-calc").prop("disabled", !1), setProgress(100)) : 2 == usl_val ? ($("narush_row").removeClass("closed"), $("#narusheniya").focus(), setProgress(80)) : ($("#klass_row").removeClass("closed"), $("#Kbm").focus(), setProgress(80))
}
function voditeliChanged(a) {
    $("#voditeli").prop("disabled", !0), $("#voditeli_clear").removeClass("closed"), resetVals(["klass", "narush"]), setProgress(85), 1 == usl_val ? ($("#btn-calc").prop("disabled", !1), setProgress(100)) : 2 == usl_val ? ($("narush_row").removeClass("closed"), $("#narusheniya").focus()) : ($("#klass_row").removeClass("closed"), $("#Kbm").focus())
}
function klassChanged(a) {
    $("#Kbm").prop("disabled", !0), $("#Kbm_clear").removeClass("closed"), resetVals(["narush"]), 1 != usl_val ? ($("#narush_row").removeClass("closed"), $("#narusheniya").focus(), setProgress(90)) : ($("#btn-calc").prop("disabled", !1), setProgress(100))
}
function narushChanged(a) {
    $("#narusheniya").prop("disabled", !0), $("#narusheniya_clear").removeClass("closed"), $("#btn-calc").prop("disabled", !1), setProgress(100)
}
function isNumeric(a) {
    return!isNaN(parseFloat(a)) && isFinite(a)
}
function openMenu(a, b) {
    $(a).toggleClass("_active"), $(b).slideToggle("fast")
}
function scrollToElement(a, b) {
    var c = a, d = b;
    isNumeric(d) && $("html, body").animate({scrollTop: $(c).offset().top}, +d)
}
function getTwoNumber(a) {
    var b = parseInt(a), c = a - b, d = new Array(b, c);
    return d
}
function getNumRazryad(a) {
    var b = a + "";
    return b.replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, "$1&thinsp;")
}
function calculate() {
    var a = "физическое лицо";
    isJur && (a = "юридическое лицо"), $("#sob_ts").html(a);
    var b = "стандартные";
    isJur ? "стандартные" != $("#usloviya_ur option:selected").text() && (b = $("#usloviya_ur option:selected").text()) : "стандартные" != $("#usloviya option:selected").text() && (b = $("#usloviya option:selected").text()), $("#usl").text(b), $("#itog_tip_ts").html($("#tip-ts option:selected").text());
    var c = 0, d = 0;
    isJur ? (c = base_arr_jur[$("#tip-ts").val()][0], d = base_arr_jur[$("#tip-ts").val()][1]) : (c = base_arr_fiz[$("#tip-ts").val()][0], d = base_arr_fiz[$("#tip-ts").val()][1]), $("#tb_1").html(getNumRazryad(c)), $("#tb_2").html(getNumRazryad(d));


    var e, f = 1, g = 2 == $("#pricep").val();
    $("#pricep_row:visible").length > 0 && (g ? (e = "Да", f = isJur ? coef_pricep_jur[$("#tip-ts").val()] : coef_pricep_fiz[$("#tip-ts").val()]) : e = "Нет", $("#pric_kof").text(f), $("#pric").text(e));
    var h = 1;
    if ($("#moshnost_row:visible").length > 0) {
        $("#mosh").html($("#moshnost option:selected").text());
        var i = $("#moshnost").val();
        h = coef_moshn[i], $("#mosh-kof").html(h)
    }
    var j, k = 1;
    if ($("#region_row:visible").length > 0) {

    var l = $("#region").val(), m = $("#city-" + l);
        m.length > 0 ? (k = "tr" == $("#tip-ts").val() ? coef_city[l][m.val()][1] : coef_city[l][m.val()][0], $("#reg-city").removeClass("closed").html(m.find("option:selected").text() + ";")) : k = "tr" == $("#tip-ts").val() ? coef_city[l].def[1] : coef_city[l].def[0], j = $("#region option:selected").text()
    } else 2 == usl_val && (j = "Иностранное государство", k = k_city_in);
    $("#reg").text(j), $("#reg_kof").text(k);

    var n = 1;
    $("#itog_period").hide(),
    $("#itog_srok").hide(),
    $("#period_fl_row:visible").length > 0 ?
        ($("#itog_period").show(), $("#per").html($("#period-fl option:selected").text()), n = coef_period[$("#period-fl").val()],  $("#per_kof").html(n)) :
    $("#period_ul_row:visible").length > 0 ?
        ($("#itog_period").show(), $("#per").html($("#period-ul option:selected").text()), n = coef_period[$("#period-ul").val()], $("#per_kof").html(n)) :
     $("#period_in_row:visible").length > 0 ?
         ($("#itog_srok").show(), $("#sr").html($("#period-in option:selected").text()), n = coef_period[$("#period-in").val()], $("#sr_kof").html(n)) :
         1 == usl_val && ($("#itog_srok").show(), $("#sr").html(k_period_transit_text), $("#sr_kof").html(k_period_transit), n = k_period_transit), isJur && 0 == usl_val && $("#itog_period").show();

    var o, p = 1 == $("#spisok").val(), q = 1.8;

    inostr ? (isJur ? (o = "неограниченный список", q = k_spisok_in_jur) : (o = "ограниченный список", q = k_spisok_in_fiz)) : (isJur ? o = "неограниченный список" : (p ? (o = "ограниченный список", q = k_spisok_lim) : (o = "неограниченный список", q = k_spisok_notlim))))

    var r, s = 1;
    2 == usl_val ?
        (s = isJur ? k_voditeli_in_jur : k_voditeli_in_fiz, r = "единое значение для иностранцев") :
        $("#voditeli_row:visible").length > 0 && (r = $("#voditeli option:selected").text(), s = coef_voditeli[$("#voditeli").val()]), $("#vod").text(r), $("#vod_kof").text(s);

    var t = 1;

    "не страховался ранее" == $("#klass") ?
        $("#klass").html("3 (не страховался ранее)") :
        $("#klass").html($("#Kbm option:selected").text()),

        t = coef_klass[$("#Kbm").val()], $("#klass_kof").html(t);

    var u, v = 0, w = 0, x = k_narush_no, y = 2 == $("#narusheniya").val();
    y ? (u = "да", x = k_narush_yes, v = c * k * 5, w = d * k * 5) : (u = "нет", v = c * k * 3, w = d * k * 3), $("#nar").text(u), $("#nar_kof").text(x);
    var z = 0,
        A = 0,
        B = $("#tip-ts").val();
    c = bas
    d =

    h = coef_moshn;
    f = isJur ? coef_pricep_jur[$("#tip-ts").val()] : coef_pricep_fiz[$("#tip-ts").val()])


    if (isJur) {
        if (0 == usl_val || 3 == usl_val) if ("b" == B || "b-t" == B) {
            z = c * k * t * k_spisok_notlim * h * n * x * f,
            A = d * k * t * k_spisok_notlim * h * n * x * f;
            var C = "ТБ × КТ × КБМ × КО × КМ × КС × КН × КПр"
        } else {
            z = c * k * t * k_spisok_notlim * f * n * x,
            A = d * k * t * k_spisok_notlim * f * n * x;
            var C = "ТБ × КТ × КБМ × КО × КС × КН × КПр"
        } else if (1 == usl_val) if ("b" == B || "b-t" == B) {
            z = c * k_spisok_notlim * h * k_period_transit * f,
            A = d * k_spisok_notlim * h * k_period_transit * f;
            var C = "ТБ × КО × КМ × КП × КПр"
        } else {
            z = c * k_spisok_notlim * k_period_transit * f,
            A = d * k_spisok_notlim * k_period_transit * f;
            var C = "ТБ × КО × КП × КПр"
        } else if (2 == usl_val) if ("b" == B || "b-t" == B) {
            z = c * k * q * h * n * x * f,
            A = d * k * q * h * n * x * f;
            var C = "ТБ × КТ × КБМ × КО × КМ × КП × КН × КПр"
        } else {
            z = c * k * q * n * x * f,
            A = d * k * q * n * x * f;
            var C = "ТБ × КТ × КБМ × КО × КП × КН × КПр"
        }
    } else if (0 == usl_val || 3 == usl_val) if ("b" == B || "b-t" == B) {
            z = c * k * t * s * q * h * n * x,
            A = d * k * t * s * q * h * n * x;
            var C = "ТБ × КТ × КБМ × КВС × КО × КМ × КС × КН"
        } else {
            z = c * k * t * s * q * f * n * x,
            A = d * k * t * s * q * f * n * x;
            var C = "ТБ × КТ × КБМ × КВС × КО × КС × КН × КПр"
        } else if (1 == usl_val) if ("b" == B || "b-t" == B) {
            z = c * s * q * h * k_period_transit,
            A = d * s * q * h * k_period_transit;
            var C = "ТБ × КВС × КО × КМ × КП"
        } else {
            z = c * s * q * k_period_transit * f,
            A = d * s * q * k_period_transit * f;
            var C = "ТБ × КВС × КО × КП × КПр"
        } else if (2 == usl_val) if ("b" == B || "b-t" == B) {
            z = c * k * s * q * h * n * x,
            A = d * k * s * q * h * n * x;
            var C = "ТБ × КТ × КБМ × КВС × КО × КМ × КН × КН"
        } else {
            z = c * k * s * q * n * x * f,
            A = d * k * s * q * n * x * f;
            var C = "ТБ × КТ × КБМ × КО × КП × КН × КПр"
    }
    var D = getNumRazryad(getTwoNumber(z)[0]), E = getTwoNumber(z)[1],
        F = getNumRazryad(getTwoNumber(A)[0]), G = getTwoNumber(A)[1],
        H = getNumRazryad(getTwoNumber(v)[0]), I = getTwoNumber(v)[1],
        J = getNumRazryad(getTwoNumber(w)[0]), K = getTwoNumber(w)[1];
    v < z || w < A ?
        ($("#stoim_1").html(H + " р. " + I.toFixed(2).slice(2) + " к."), $("#stoim_2").html(J + " р. " + K.toFixed(2).slice(2) + " к."), $("#itog-stoimost-max").removeClass("closed")) :
        ($("#stoim_1").html(D + " р. " + E.toFixed(2).slice(2) + " к."), $("#stoim_2").html(F + " р. " + G.toFixed(2).slice(2) + " к.")), $("#formula").html(C), $("#itog").removeClass("closed")
}
var base_arr_jur = {
    a: [867, 1579],
    b: [2573, 3087],
    "b-t": [5138, 6166],
    c: [3509, 4211],
    "c-m": [5284, 6341],
    d: [2808, 3370],
    "d-m": [3509, 4211],
    "d-t": [5138, 6166],
    tb: [2808, 3370],
    tm: [1751, 2101],
    tr: [1124, 1579]
};
var base_arr_fiz = {
    a: [867, 1579],
    b: [3432, 4118],
    "b-t": [5138, 6166],
    c: [3509, 4211],
    "c-m": [5284, 6341],
    d: [2808, 3370],
    "d-m": [3509, 4211],
    "d-t": [5138, 6166],
    tb: [2808, 3370],
    tm: [1751, 2101],
    tr: [1124, 1579]
};
var coef_city = {
    1: {def: [1.3, 1]},
    2: {"2_1": [1.3, .8],
        "2_2": [.7, .5]},
    3: {"3_1": [1.2, .8],
        "3_2": [1.1, .8],
        "3_3": [1.3, .8],
        "3_4": [1.8, 1],
        "3_5": [1, .8]},
    4: {"4_1": [1.3, .8],
        "4_2": [.6, .5]},
    5: {"5_1": [.7, .5],
        "5_2": [.6, .5]},
    6: {"6_1": [.8, .5],
        "6_2": [.6, .5],
        "6_3": [.6, .5]},
    7: {"7_1": [1, .8],
        "7_2": [.7, .5]},
    8: {"8_1": [1.3, .8],
        "8_2": [.6, .5]},
    9: {def: [1, .8]},
    10: {"10_1": [1.3, .8],
        "10_2": [.8, .5]},
    11: {"11_1": [1.6, 1],
        "11_2": [1.3, .8],
        "11_3": [1, .8]},
    12: {"12_1": [.6, .6],
        "12_2": [.6, .6]},
    13: {"13_1": [1, .8],
        "13_2": [1.4, .8],
        "13_3": [.7, .5]},
    14: {"14_1": [1.2, 1],
        "14_2": [1.5, 1],
        "14_3": [.8, .6]},
    15: {"15_1": [.8, .5],
        "15_2": [1.2, .7],
        "15_3": [.6, .5]},
    16: {"16_1": [1, .8],
        "16_2": [.8, .5]},
    17: {"17_1": [1.3, .8],
        "17_2": [1, .8],
        "17_3": [1.2, .8],
        "17_4": [2, 1.2],
        "17_5": [1.7, 1],
        "17_6": [1.1, .8]},
    18: {"18_1": [.6, .5],
        "18_2": [.6, .5]},
    19: {"19_1": [1.1, .8],
        "19_2": [1, .8],
        "19_3": [1.6, 1],
        "19_4": [.8, .5]},
    20: {"20_1": [1, .8],
        "20_2": [.6, .5]},
    21: {def: [.6, .5]},
    22: {"22_1": [1.1, .8],
        "22_2": [1.2, .8],
        "22_3": [1.7, 1],
        "22_4": [.8, .5]},
    23: {"23_1": [1.7, 1],
        "23_2": [1.2, .8],
        "23_3": [1.1, .8],
        "23_4": [.7, .5]},
    24: {"24_1": [.6, .5],
        "24_2": [.7, .5],
        "24_3": [.6, .5]},
    25: {"25_1": [1.3, 1],
        "25_2": [1, .6]},
    26: {"26_1": [1.3, .8],
        "26_2": [1.2, .8],
        "26_3": [1.1, .8],
        "26_4": [1.8, 1],
        "26_5": [1, .8]},
    27: {"27_1": [1.1, .8],
        "27_2": [1.3, .8],
        "27_3": [1, .8],
        "27_4": [1.8, 1],
        "27_5": [.9, .5]},
    28: {"28_1": [1.3, .8],
        "28_2": [1, .8],
        "28_3": [2, 1.2],
        "28_4": [1.2, .8],
        "28_5": [1.1, .8]},
    29: {"29_1": [1, .8],
        "29_2": [1.4, 1],
        "29_3": [.7, .5]},
    30: {"30_1": [1, .8],
        "30_2": [1.2, .8],
        "30_3": [.7, .5]},
    31: {"31_1": [1, .8],
        "31_2": [1.3, .8],
        "31_3": [1.7, 1],
        "31_4": [.8, .5]},
    32: {"32_1": [1.1, .9],
        "32_2": [1.6, .9],
        "32_3": [1, .6]},
    33: {"33_1": [1.8, 1],
        "33_2": [1.6, 1],
        "33_3": [1.7, 1],
        "33_4": [.85, .5]},
    34: {"34_1": [1.4, 1],
        "34_2": [.8, .5]},
    35: {"35_1": [1.3, .8],
        "35_2": [1, .8],
        "35_3": [.8, .5]},
    36: {"36_1": [1.5, 1],
        "36_2": [1, .8],
        "36_3": [.7, .5]},
    37: {"37_1": [1.6, 1],
        "37_2": [1.1, .8],
        "37_3": [1.2, .8],
        "37_4": [1, .8]},
    38: {"38_1": [1.3, .8],
        "38_2": [1.1, .8],
        "38_3": [1, .8],
        "38_4": [.7, .5]},
    39: {"39_1": [1.7, 1],
        "39_2": [1.8, 1],
        "39_3": [.9, .5]},
    40: {"40_1": [1.1, .9],
        "40_2": [1.5, 1.1],
        "40_3": [.8, .6]},
    41: {"41_1": [1.8, 1],
        "41_2": [1.1, .8],
        "41_3": [1, .8],
        "41_4": [.9, .5]},
    42: {"42_1": [1.2, .8],
        "42_2": [1, .8],
        "42_3": [1.7, 1],
        "42_4": [1.1, .8],
        "42_5": [1.3, .8],
        "42_6": [.8, .5]},
    43: {"43_1": [1.1, .8],
        "43_2": [.8, .5]},
    44: {"44_1": [1.2, .8],
        "44_2": [1.3, .8],
        "44_3": [.9, .5]},
    45: {"45_1": [1.2, .8],
        "45_2": [1.3, .8],
        "45_3": [1.9, 1],
        "45_4": [1.8, 1],
        "45_5": [1.1, .8]},
    46: {"46_1": [1.4, 1],
        "46_2": [1.2, .8],
        "46_3": [.8, .5]},
    47: {"47_1": [1.3, .8],
        "47_2": [.7, .5]},
    48: {"48_1": [1.4, .8],
        "48_2": [1.1, .8],
        "48_3": [.6, .5]},
    49: {"49_1": [1, .8],
        "49_2": [1.2, .8],
        "49_3": [.7, .5]},
    50: {def: [1.3, .8]},
    51: {"51_1": [1, .8],
        "51_2": [1.5, 1],
        "51_3": [.8, .5]},
    52: {"52_1": [.7, .5],
        "52_2": [.6, .5]},
    53: {def: [1.7, 1]},
    54: {"54_1": [1.3, 1],
        "54_2": [2.1, 1.2],
        "54_3": [1.6, 1],
        "54_4": [1.2, 1]},
    55: {"55_1": [1.1, .8],
        "55_2": [1.3, .8],
        "55_3": [1.2, .8],
        "55_4": [1.8, 1],
        "55_5": [1, .8]},
    56: {"56_1": [1, .8],
        "56_2": [1.3, .8],
        "56_3": [.9, .5]},
    57: {"57_1": [1.3, .8],
        "57_2": [1.2, .8],
        "57_3": [1, .8],
        "57_4": [1.7, 1],
        "57_5": [.9, .5]},
    58: {"58_1": [1.6, 1],
        "58_2": [.9, .5]},
    59: {"59_1": [1, .8],
        "59_2": [1.7, 1],
        "59_3": [1.1, .8],
        "59_4": [.8, .5]},
    60: {"60_1": [1, .8],
        "60_2": [1.2, .8],
        "60_3": [.7, .5]},
    61: {"61_1": [1.2, .8],
        "61_2": [1, .8],
        "61_3": [1.4, 1],
        "61_4": [.7, .5]},
    62: {"62_1": [1, .8],
        "62_2": [1.2, .8],
        "62_3": [.7, .5]},
    63: {"63_1": [1.2, .8],
        "63_2": [1.3, .8],
        "63_3": [1, .8],
        "63_4": [1.8, 1],
        "63_5": [1.1, .8],
        "63_6": [.8, .5]},
    64: {"64_1": [1.4, 1],
        "64_2": [.9, .5]},
    65: {"65_1": [1.1, .8],
        "65_2": [1.6, 1],
        "65_3": [1.5, 1],
        "65_4": [1.2, .8],
        "65_5": [.9, .5]},
    66: {"66_1": [1, .8],
        "66_2": [1.6, 1],
        "66_3": [1.2, .8],
        "66_4": [.7, .5]},
    67: {"67_1": [1.5, 1],
        "67_2": [.9, .5]},
    68: {"68_1": [1.1, .8],
        "68_2": [1.3, .8],
        "68_3": [1.2, .8],
        "68_4": [1.8, 1],
        "68_5": [1, .8]},
    69: {"69_1": [1, .8],
        "69_2": [1.2, .8],
        "69_3": [.7, .5]},
    70: {"70_1": [1, .8],
        "70_2": [1.2, .8],
        "70_3": [.8, .5]},
    71: {"71_1": [1, .8],
        "71_2": [1.5, 1],
        "71_3": [.8, .5]},
    72: {"72_1": [1.2, .8],
        "72_2": [1.6, 1],
        "72_3": [.9, .5]},
    73: {"73_1": [1, .8],
        "73_2": [1.5, 1],
        "73_3": [1.2, .8],
        "73_4": [.9, .5]},
    74: {"74_1": [1.3, .8],
        "74_2": [2, 1.2],
        "74_3": [1.1, .8]},
    75: {"75_1": [1.2, .9],
        "75_2": [1.5, 1.1],
        "75_3": [.9, .6]},
    76: {"76_1": [1.4, .8],
        "76_2": [1.6, 1],
        "76_3": [1.8, 1],
        "76_4": [1.2, .8],
        "76_5": [2.1, 1.3],
        "76_6": [1, .8]},
    77: {"77_1": [1.5, 1],
        "77_2": [.9, .5]},
    78: {def: [2, 1.2]},
    79: {def: [1.8, 1]},
    80: {def: [.6, .6]},
    81: {"81_1": [.6, .5],
        "81_2": [.6, .5]},
    82: {def: [.8, .5]},
    83: {"83_1": [1, .8],
        "83_2": [1.3, .8],
        "83_3": [2, 1.2],
        "83_4": [1.8, 1],
        "83_5": [1.5, 1],
        "83_6": [1.1, .8]},
    84: {def: [.6, .5]},
    85: {"85_1": [1, .8],
        "85_2": [1.7, 1],
        "85_3": [1.1, .8]},
    86: {def: [.6, .5]}
};

var k_city_in = 1.7,
    coef_period = {3: .5, 4: .6, 5: .65, 6: .7, 7: .8, 8: .9, 9: .95, 10: 1, 2: .4, 1: .3, 0: .2},
    k_period_transit = .2,
    k_period_transit_text = "до 20 дней",
    coef_voditeli = {0: 1, 1: 1.7, 2: 1.6, 3: 1.8},
    k_voditeli_in_jur = 1,
    k_voditeli_in_fiz = 1.7,
    coef_klass = {m: 2.45, 0: 2.3, 1: 1.55, 2: 1.4, 3: 1, 4: .95, 5: .9, 6: .85, 7: .8, 8: .75, 9: .7, 10: .65, 11: .6, 12: .55, 13: .5, def: 1},
    coef_pricep_jur = {a: 1.16, b: 1.16, "b-t": 1, c: 1.4, "c-m": 1.25, d: 1, "d-m": 1, "d-t": 1, tb: 1, tm: 1, tr: 1.24},
    coef_pricep_fiz = {a: 1.16, b: 1.16, "b-t": 1, c: 1.4, "c-m": 1.25, d: 1, "d-m": 1, "d-t": 1, tb: 1, tm: 1, tr: 1.24},
    coef_moshn = {0: .6, 1: 1, 2: 1.1, 3: 1.2, 4: 1.4, 5: 1.6},
    k_spisok_in_jur = 1.8,
    k_spisok_in_fiz = 1,
    k_spisok_lim = 1,
    k_spisok_notlim = 1.8,
    k_narush_yes = 1.5,
    k_narush_no = 1,
    isJur = !1,
    isSpisokLimited = !0,
    isPricep = !1,
    hasNarush = !1,
    usl_val = "";


$(document).ready(function () {
    setFormEnabled(!0), resetVals(["jur"]), $("#vladelec").change(function () {
        this.value != -1 && setJur(2 == this.value)
    }), $("#usloviya").change(function () {
        uslovieChanged(this.value)
    }), $("#usloviya_ur").change(function () {
        uslovieChanged(this.value)
    }), $("#tip-ts").change(function () {
        tipTSChanged(this.value)
    }), $("#moshnost").change(function () {
        moshnostChanged(this.value)
    }), $("#pricep").change(function () {
        pricepChanged(this.value)
    }), $("#region").change(function () {
        regionChanged(this.value)
    }), $('select[name*="city-"]').change(function () {
        cityChanged(this.value)
    }), $("#period-fl").change(function () {
        periodChanged(this.value)
    }), $("#period-ul").change(function () {
        periodChanged(this.value)
    }), $("#period-in").change(function () {
        periodChanged(this.value)
    }), $("#spisok").change(function () {
        spisokChanged(this.value)
    }), $("#voditeli").change(function () {
        voditeliChanged(this.value)
    }), $("#Kbm").change(function () {
        klassChanged(this.value)
    }), $("#narusheniya").change(function () {
        narushChanged(this.value)
    }), $("#vladelec_clear").click(function () {
        resetVals(["jur"]), setFormEnabled(!0), $("#usl_row").addClass("closed"), $("#tip_ts_row").addClass("closed"), $("#moshnost_row").addClass("closed"), $("#pricep_row").addClass("closed"), $("#region_row").addClass("closed"), $("#city_row").addClass("closed"), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), $("#vladelec").focus(), setProgress(0), $("#progress-bar").removeClass("end")
    }), $("#usloviya_clear").click(function () {
        resetVals(["uslovie"]), $("#usloviya").prop("disabled", !1), $("#usloviya_ur").prop("disabled", !1), $("#tip-ts").prop("disabled", !1), $("#moshnost").prop("disabled", !1), $("#pricep").prop("disabled", !1), $("#region").prop("disabled", !1), $('select[name*="city-"]').prop("disabled", !1), $("#period-fl").prop("disabled", !1), $("#period-ul").prop("disabled", !1), $("#period-in").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#tip_ts_row").addClass("closed"), $("#moshnost_row").addClass("closed"), $("#pricep_row").addClass("closed"), $("#region_row").addClass("closed"), $("#city_row").addClass("closed"), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(10), $("#progress-bar").removeClass("end")
    }), $("#tip-ts_clear").click(function () {
        resetVals(["tip-ts"]), $("#tip-ts").prop("disabled", !1), $("#moshnost").prop("disabled", !1), $("#pricep").prop("disabled", !1), $("#region").prop("disabled", !1), $('select[name*="city-"]').prop("disabled", !1), $("#period-fl").prop("disabled", !1), $("#period-ul").prop("disabled", !1), $("#period-in").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#moshnost_row").addClass("closed"), $("#pricep_row").addClass("closed"), $("#region_row").addClass("closed"), $("#city_row").addClass("closed"), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(20), $("#progress-bar").removeClass("end")
    }), $("#moshnost_clear").click(function () {
        resetVals(["moshnost"]), $("#moshnost").prop("disabled", !1), $("#pricep").prop("disabled", !1), $("#region").prop("disabled", !1), $('select[name*="city-"]').prop("disabled", !1), $("#period-fl").prop("disabled", !1), $("#period-ul").prop("disabled", !1), $("#period-in").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#pricep_row").addClass("closed"), $("#region_row").addClass("closed"), $("#city_row").addClass("closed"), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(30), $("#progress-bar").removeClass("end")
    }), $("#pricep_clear").click(function () {
        resetVals(["pricep"]), $("#pricep").prop("disabled", !1), $("#region").prop("disabled", !1), $('select[name*="city-"]').prop("disabled", !1), $("#period-fl").prop("disabled", !1), $("#period-ul").prop("disabled", !1), $("#period-in").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#region_row").addClass("closed"), $("#city_row").addClass("closed"), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(40), $("#progress-bar").removeClass("end")
    }), $("#region_clear").click(function () {
        resetVals(["region"]), $("#region").prop("disabled", !1), $('select[name*="city-"]').prop("disabled", !1), $("#period-fl").prop("disabled", !1), $("#period-ul").prop("disabled", !1), $("#period-in").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#city_row").addClass("closed"), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(50), $("#progress-bar").removeClass("end")
    }), $("#city_clear").click(function () {
        resetVals(["city"]), $('select[name*="city-"]').prop("disabled", !1), $("#period-fl").prop("disabled", !1), $("#period-ul").prop("disabled", !1), $("#period-in").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(60), $("#progress-bar").removeClass("end")
    }), $("#period-fl_clear").click(function () {
        resetVals(["period"]), $("#period-fl").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(65), $("#progress-bar").removeClass("end")
    }), $("#period-ul_clear").click(function () {
        resetVals(["period"]), $("#period-ul").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(65), $("#progress-bar").removeClass("end")
    }), $("#period-in_clear").click(function () {
        resetVals(["period"]), $("#period-in").prop("disabled", !1), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(65), $("#progress-bar").removeClass("end")
    }), $("#spisok_clear").click(function () {
        resetVals(["spisok"]), $("#spisok").prop("disabled", !1), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(70), $("#progress-bar").removeClass("end")
    }), $("#voditeli_clear").click(function () {
        resetVals(["voditeli"]), $("#voditeli").prop("disabled", !1), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#progress-bar").removeClass("end"), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(75), $("#progress-bar").removeClass("end")
    }), $("#Kbm_clear").click(function () {
        resetVals(["klass"]), $("#Kbm").prop("disabled", !1), $("#narusheniya").prop("disabled", !1), $("#narush_row").addClass("closed"), $("#btn-calc").prop("disabled", !0), $("#progress-bar").removeClass("end"), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(80), $("#progress-bar").removeClass("end")
    }), $("#narusheniya_clear").click(function () {
        resetVals(["narush"]), $("#narusheniya").prop("disabled", !1), $("#btn-calc").prop("disabled", !0), $("#progress-bar").removeClass("end"), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), setProgress(90), $("#progress-bar").removeClass("end")
    }), $("#btn-reset").click(function () {
        resetVals(["jur"]), setFormEnabled(!0), $("#usl_row").addClass("closed"), $("#tip_ts_row").addClass("closed"), $("#moshnost_row").addClass("closed"), $("#pricep_row").addClass("closed"), $("#region_row").addClass("closed"), $("#city_row").addClass("closed"), $("#period_fl_row").addClass("closed"), $("#period_ul_row").addClass("closed"), $("#period_in_row").addClass("closed"), $("#spisok_row").addClass("closed"), $("#voditeli_row").addClass("closed"), $("#klass_row").addClass("closed"), $("#narush_row").addClass("closed"), $("#itog").addClass("closed"), $("#itog-stoimost").removeClass("closed"), $("#reg-city").addClass("closed"), setProgress(0), $("#progress-bar").removeClass("end"), scrollToElement("#calc-osago", 600), $("#btn-reset").addClass("closed"), $("#btn-calc").removeClass("closed")
    }), $("#btn-calc").click(function () {
        setFormEnabled(!1), updateItogRows(), calculate(), $("#progress-bar").addClass("end"), $("#btn-calc").addClass("closed").prop("disabled", !0), $("#btn-reset").removeClass("closed").prop("disabled", !1), $("#vladelec_clear").addClass("closed"), $("#usloviya_clear").addClass("closed"), $("#tip-ts_clear").addClass("closed"), $("#moshnost_clear").addClass("closed"), $("#pricep_clear").addClass("closed"), $("#region_clear").addClass("closed"), $("#city_clear").addClass("closed"), $("#period-fl_clear").addClass("closed"), $("#period-ul_clear").addClass("closed"), $("#period-in_clear").addClass("closed"), $("#spisok_clear").addClass("closed"), $("#voditeli_clear").addClass("closed"), $("#Kbm_clear").addClass("closed"), $("#narusheniya_clear").addClass("closed"), scrollToElement("#itog", 600)
    })
});