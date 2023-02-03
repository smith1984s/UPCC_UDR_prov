'''
Created on 6 янв. 2023 г.

@author: denis
'''

profile_template = {
  "SID": "288755DBEFD7A8FA",
  "PCRFINDEX": "0",
  "SUBSCRIBERSN": "2807687AEFD7B0DE",
  "SUBSCRIBERIDENTIFIER": "",
  "MSISDN": "",
  "STATUS": "1",
  "PAIDTYPE": "254",
  "STATION": "2",
  "CONTACTMETHOD": "3",
  "BILLINGCYCLEDAY": "255",
  "DOMAINNAME": "default1",
  "DOMAINID": "0000000000000063",
  "SPNAME": "default1",
  "SPID": "0000000000000063",
  "CUSTOMERATTR": "0",
  "USRSUBNETTYPE": "0",
  "LANGUAGE": "255",
  "SMSRECEIVEFLAG": "0",
  "FLAG": "0",
  "GBRUL": "0",
  "GBRDL": "0",
  "PACKAGETYPE": "255",
  "NEXTRESETDATETIME": "FFFFFFFFFFFFFF"
}

multi_fields = {
    "quota" : (
        "\tQUOTA=411199-DATA_S_Quota&E724C3EDA186C92E&524288000&524288000&0&1&20221217163525&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1671273325&1;",
        "\tQUOTA=413102-DATA_D_Quota&E7242330DC433136&1024&0&0&6&20221031224415&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1667234655&1;",
        "\tQUOTA=409239-DATA_D_Quota&E72483489A86C92E&1024&4625803&179066641&1&20220715215813&FFFFFFFFFFFFFF&0&255&0&0&0&0&1&0&0&179066641&0&1672248611&1;",
        "\tQUOTA=CLONE-4110813-DATA_D_Quota&E72483D8A186C92E&25165824&25151084&14740&1&20221201021813&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&14740&0&1671942913&1;",
        "\tQUOTA=CLONE-4110811-DATA_D_Quota&E72403E2A186C92E&209715200&134567925&75147275&1&20221201021813&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&75147275&0&1671943899&1;",
        "\tQUOTA=411148-DATA_D_Quota&E72443E0A186C92E&1024&13709341&18068980&1&20221222232502&FFFFFFFFFFFFFF&0&255&0&0&0&0&1&0&0&18068980&0&1672285643&1;",
        "\tQUOTA=405244-DATA_D_Quota&73C98606EC93E412&20971520&0&22639801&6&20221211183044&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&22639801&0&1671541445&1;",
        "\tQUOTA=405244-DATA_S_Quota&73C91A06AE7DE312&524288000&494345729&29942271&1&20221211183044&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&29942271&0&1672285001&1;",
        "\tQUOTA=413102-DATA_D_Quota&E7242330DC433136&1024&0&0&6&20221026210615&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1666796775&1;",
        "\tQUOTA=408877-DATA_D_Quota&E74CE30310F8B92E&5242880&19669480&0&1&20221219005125&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1671389490&1;",
        "\tQUOTA=412303-DATA_D_Quota&E7248322DC433136&1024&0&1172&6&20221018201301&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&1172&0&1667974325&1;",
        "\tQUOTA=413548-DATA_D_Quota&E74CA327D21BFD35&2097152&2097152&0&1&20221220163153&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1671532313&1;",
        "\tQUOTA=410578-DATA_D_Quota&E7246377A186C92E&1024&585829&1511323&1&20221211105534&FFFFFFFFFFFFFF&0&255&0&0&0&0&1&0&0&1511323&0&1672251157&1;",
        "\tQUOTA=411741-DATA_D_Quota&E72423B7B586C92E&1048576&0&1048627&6&20221118135223&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&1048627&0&1668924405&1;",
        "\tQUOTA=408877-DATA_S_Quota&E74C230410F8B92E&524288000&524288000&0&1&20221219005125&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1671389485&1;",
        "\tQUOTA=408878-DATA_D_Quota&E74C230310F8B92E&10485760&44040192&0&1&20221223011556&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1671736559&1;",
        "\tQUOTA=410658-DATA_D_Quota&E724C384A186C92E&524288000&524288000&0&1&20221220150940&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1671527380&1;",
        "\tQUOTA=411742-DATA_D_Quota&E724A3B7B586C92E&2097152&2088450&8702&1&20221123011414&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&8702&0&1671679628&1;",
        "\tQUOTA=408878-DATA_S_Quota&E74C630310F8B92E&524288000&524288000&0&1&20221223011556&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1671736556&1;",
        "\tQUOTA=411663-DATA_S_Quota&E74C2311D21BFD35&524288000&524288000&0&1&20221230011844&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1672341524&1;",
        "\tQUOTA=4045471-DATA_D_Quota&73C9E216E7D1EE13&12582912&11569018&1013894&1&20221229004055&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&1013894&0&1672323915&1;",
        "\tQUOTA=408960-DATA_D_Quota&E724A3419A86C92E&12582912&12558351&24561&1&20221213132033&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&24561&0&1671374934&1;",
        "\tQUOTA=408960-DATA_S_Quota&E72463429A86C92E&52428800&52428284&516&1&20221213132033&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&516&0&1671374934&1;",
        "\tQUOTA=413102-DATA_D_Quota&E7242330DC433136&1024&12463892&0&1&20221107164441&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1670439735&1;",
        "\tQUOTA=409239-DATA_D_Quota&E72483489A86C92E&1024&0&65013247&6&20220926020637&FFFFFFFFFFFFFF&0&255&0&0&0&0&1&0&0&65013247&0&1671513741&1;",
        "\tQUOTA=40777900081-DATA_D_Quota&E72423EAF0FAB828&52428800&51563731&865069&1&20221230004352&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&865069&0&1672370562&1;",
        "\tQUOTA=413102-DATA_D_Quota&E7242330DC433136&1024&0&0&6&20221031102855&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&0&0&1667190535&1;",
        "\tQUOTA=413548-DATA_D_Quota&E74CA327D21BFD35&2097152&0&2097179&6&20221223152136&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&2097179&0&1672240051&1;",
        "\tQUOTA=408377-DATA_D_Quota&E724430BF1FAB828&1024&8388608&0&1&20221229141545&FFFFFFFFFFFFFF&0&255&0&0&0&0&1&0&0&0&0&1672301745&1;",
        "\tQUOTA=CLONE-4110811-DATA_D_Quota&E72403E2A186C92E&209715200&188384384&21330816&1&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&255&65535&65535&65535&0&0&0&0&21330816&1&1671943899&1;",
        "\tQUOTA=CLONE-4110813-DATA_D_Quota&E72483D8A186C92E&12582912&12568172&14740&1&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&255&65535&65535&65535&0&0&0&0&14740&1&1671942913&1;",
        "\tQUOTA=412303-DATA_D_Quota&E7248322DC433136&1024&0&1067&6&20221218222935&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&1067&0&1671499589&1;",
        "\tQUOTA=410678-DATA_S_Quota&E724838FA186C92E&204800&199410&5390&1&20221218222935&FFFFFFFFFFFFFF&0&255&0&0&0&0&0&0&0&5390&0&1671691673&1;"
        ),
    "subscr" : (
        "\tSUBSCRIPTION=Default_Service&73C9D2015130600A&1&20220605191622&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=411199&E724C3EAA186C92E&1&20221217163525&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&545&0&1&0&0&1;",
        "\tSUBSCRIPTION=409239&E724E3489A86C92E&1&20220715215813&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&68&0&1&0&0&1;",
        "\tSUBSCRIPTION=413102&E7248330DC433136&1&20221031224415&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&179&0&1&0&0&1;",
        "\tSUBSCRIPTION=CLONE-4110813&E724A3D8A186C92E&1&20221201021813&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3D8A186C92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&502&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20220909154147&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&820&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service&73C9D2015130600A&1&20220930135347&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=CLONE-4110811&E72443D8A186C92E&1&20221201021813&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3D8A186C92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&502&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Limit_Redirect&E72463099A86C92E&1&20221201021813&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3D8A186C92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&502&0&1&0&0&1;",
        "\tSUBSCRIPTION=4052443&73C916065A7DE312&1&20221211183044&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&73C95206D694E312&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&791&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Limit2_Redirect_ALT&73C9F2077FE9FB12&1&20221211183044&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&73C95206D694E312&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&791&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service&73C9D2015130600A&1&20181205212941&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=411148&E724A3E0A186C92E&1&20221222232502&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&91&0&1&0&0&1;",
        "\tSUBSCRIPTION=405244&73C99206ED93E412&1&20221211183044&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&73C95206D694E312&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&791&0&1&0&0&1;",
        "\tSUBSCRIPTION=413102&E7248330DC433136&1&20221026210615&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&568&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20220927115146&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&615&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20210109115358&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&761&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service_Redirect_T2&73D39A19F4966611&1&20221230061308&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Limit_Redirect&E72463099A86C92E&1&20221219005125&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E74C830410F8B92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&584&0&1&0&0&1;",
        "\tSUBSCRIPTION=413548&E74C0328D21BFD35&1&20221220163153&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&870&0&1&0&0&1;",
        "\tSUBSCRIPTION=4088771&E74C030410F8B92E&1&20221219005125&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E74C830410F8B92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&584&0&1&0&0&1;",
        "\tSUBSCRIPTION=411741&E72483B7B586C92E&1&20221118135223&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&484&0&1&0&0&1;",
        "\tSUBSCRIPTION=4088773&E74C630410F8B92E&1&20221219005125&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E74C830410F8B92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&584&0&1&0&0&1;",
        "\tSUBSCRIPTION=410578&E724C377A186C92E&1&20221211105534&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&463&0&1&0&0&1;",
        "\tSUBSCRIPTION=412303&E724C322DC433136&1&20221018201301&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&732&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service_Redirect_T2&73D39A19F4966611&1&20221023091737&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20220905112140&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&698&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Limit_Redirect&E72463099A86C92E&1&20221223011556&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E74CC30310F8B92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&392&0&1&0&0&1;",
        "\tSUBSCRIPTION=410658&E724A384A186C92E&1&20221220150940&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&973&0&1&0&0&1;",
        "\tSUBSCRIPTION=411663&E74C230FD21BFD35&1&20221230011844&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&295&0&1&0&0&1;",
        "\tSUBSCRIPTION=4088781&E74C430310F8B92E&1&20221223011556&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E74CC30310F8B92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&392&0&1&0&0&1;",
        "\tSUBSCRIPTION=4088783&E74CA30310F8B92E&1&20221223011556&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E74CC30310F8B92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&392&0&1&0&0&1;",
        "\tSUBSCRIPTION=411742&E72403B8B586C92E&1&20221123011414&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&145&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Limit_Redirect_ALT&73C9C2010A377C12&1&20221229004055&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&73C9EA16EAD1EE13&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&732&0&1&0&0&1;",
        "\tSUBSCRIPTION=405768&73C95A1264478813&1&20190619091106&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&140&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service&73C9D2015130600A&1&20221118132301&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service_Block&73C9C616A4CCEE13&1&20221229004055&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&73C9EA16EAD1EE13&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&732&0&1&0&0&1;",
        "\tSUBSCRIPTION=4045471&73C9E616E7D1EE13&1&20221229004055&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&73C9EA16EAD1EE13&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&732&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Limit_Redirect&E72463099A86C92E&1&20221213132033&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3429A86C92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&440&0&1&0&0&1;",
        "\tSUBSCRIPTION=4089601&E72443429A86C92E&1&20221213132033&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3429A86C92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&440&0&1&0&0&1;",
        "\tSUBSCRIPTION=413102&E7248330DC433136&1&20221107164441&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&586&0&1&0&0&1;",
        "\tSUBSCRIPTION=4089603&E724A3429A86C92E&1&20221213132033&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3429A86C92E&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&440&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20220314104136&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&828&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service&73C9D2015130600A&1&20220810145953&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=409239&E724E3489A86C92E&1&20220926020637&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&796&0&1&0&0&1;",
        "\tSUBSCRIPTION=407779100081&E72443EAF0FAB828&1&20221230004352&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3E9F0FAB828&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&849&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20191219105436&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&650&0&1&0&0&1;",
        "\tSUBSCRIPTION=413102&E7248330DC433136&1&20221031102855&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&444&0&1&0&0&1;",
        "\tSUBSCRIPTION=405543&E724E353F0FAB828&1&20221227004527&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&39&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service&73C9D2015130600A&1&20190901001925&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Limit_Redirect_ALT&73C9C2010A377C12&1&20221230004352&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&E724C3E9F0FAB828&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&849&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20191220142645&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&650&0&1&0&0&1;",
        "\tSUBSCRIPTION=405520&73C9CA18D3E43014&1&20221217055826&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&369&0&1&0&0&1;",
        "\tSUBSCRIPTION=413548&E74C0328D21BFD35&1&20221223152136&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&507&0&1&0&0&1;",
        "\tSUBSCRIPTION=408377&E724A30BF1FAB828&1&20221229141545&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&46&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service_Redirect_T2&73D39A19F4966611&1&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20220930134654&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&409&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service&73C9D2015130600A&1&20220930134507&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=405421&73C9B207F4CFFB12&1&20220824120320&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&695&0&1&0&0&1;",
        "\tSUBSCRIPTION=sleep_roam&E7244332E6FAB828&1&20221218222935&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&641&0&1&0&0&1;",
        "\tSUBSCRIPTION=410678&E724438FA186C92E&1&20221218222935&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&731&0&1&0&0&1;",
        "\tSUBSCRIPTION=Default_Service_Redirect_T2&73D39A19F4966611&1&20221218223326&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&1&1&FFFFFFFFFFFFFFFF&255&1&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&0&0&1&0&0&1;",
        "\tSUBSCRIPTION=412303&E724C322DC433136&1&20221218222935&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&2&1&FFFFFFFFFFFFFFFF&255&0&255&256&FFFFFFFFFFFFFFFF&0&0&128&1&255&255&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&0&251&0&1&0&0&1;"
),
 "pkgsubscr" : (
         "\tPKGSUBSCRIPTION=40777900081&E724C3E9F0FAB828&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&255&128;",
         "\tPKGSUBSCRIPTION=408960&E724C3429A86C92E&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&255&128;",
         "\tPKGSUBSCRIPTION=404547&73C9EA16EAD1EE13&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&255&128;",
         "\tPKGSUBSCRIPTION=408878&E74CC30310F8B92E&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&255&128;",
         "\tPKGSUBSCRIPTION=408877&E74C830410F8B92E&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&255&128;",
         "\tPKGSUBSCRIPTION=405244&73C95206D694E312&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&255&128;",
         "\tPKGSUBSCRIPTION=CLONE-411081&E724C3D8A186C92E&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&FFFFFFFFFFFFFF&255&128;",          
     )   
}

