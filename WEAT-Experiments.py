from WEAT import call
import wordSets as ws
import logging, os, util
from gensim.models import KeyedVectors


''' 
WEAT execution on predefined word sets from previous literature on several different models.
The model can be loaded by the "load_model" script or manually alternatively.
The functions below are organised by source.
'''


########################################################################################################################
########################################################################################################################


def greenwald(model, m_name, lower=False):
    """
    Conduct all WEAT comparisons of the nosek_harvest paper on the given model and save it in a text file in directory
    :param model:   Model to conduct the experiment
    :param m_name:  Model tag
    :return:        None
    """
    file = open('./OUT_weat/greenwald/' + m_name + '#greenwaldB.txt', 'w')
    print(lower)
    print('#######################')

    # Experiment 1
    #file.writelines(call(model, ws.gw_flow, ws.gw_insec, ws.gw_pos, ws.gw_neg, 'gw_flowInsec', lower_case=lower))
    #file.writelines(call(model, ws.gw_instr, ws.gw_weapon, ws.gw_pos, ws.gw_neg, 'gw_instrWeap_posneg', lower_case=lower))

    # Experiment 2
    file.writelines(call(model, ws.gw_Korean_names, ws.gw_Japanese_names, ws.gw_pos, ws.gw_neg, 'gw_japaneseKorean', lower_case=lower))
    file.writelines(call(model, ws.gw_Korean_names, ws.gw_Truncated_Japanese_names, ws.gw_pos, ws.gw_neg, 'gw_japaneseKorean_truncted', lower_case=lower))

    # Experiment 3
    file.writelines(call(model, ws.gw_White_American_male_names, ws.gw_Black_American_male_names, ws.gw_pos, ws.gw_neg, 'gw_blackWhite_male', lower_case=lower))
    file.writelines(call(model, ws.gw_White_American_female_names, ws.gw_Black_American_female_names, ws.gw_pos, ws.gw_neg, 'gw_blackWhite_female', lower_case=lower))
    file.writelines(call(model, ws.European_American, ws.African_American, ws.gw_pos, ws.gw_neg, 'gw_blackWhite_MF', lower_case=lower))

    file.close()


def greenwald_asian(model, m_name, lower=False):    # Experiment 2
    file = open('./OUT_weat/' + m_name + '#greenwald_asianNames.txt', 'w')

    korean = [name for name in ws.gw_Korean_names] #if name in model]
    japanese = [name for name in ws.gw_Japanese_names] # if name in model]
    japanese_t = [name for name in ws.gw_Truncated_Japanese_names] # if list in model]

    if korean and japanese:
        file.writelines(call(model, korean, japanese, ws.gw_pos, ws.gw_neg, 'gw_japaneseKorean', lower_case=lower))
    else:
        logging.error('korean or japanese empty')
    if korean and japanese_t:
        file.writelines(call(model, korean, japanese_t, ws.gw_pos, ws.gw_neg, 'gw_japaneseKorean_truncted', lower_case=lower))
    else:
        logging.error('japanese truncated empty')

    file.close()


def greenwald_black_white(model, m_name, lower=False):    # Experiment 3
    file = open('./OUT_weat/' + m_name + '#greenwald_blackWhite.txt', 'w')

    white_m = [x for x in ws.gw_White_American_male_names] # if x in model]
    white_f = [x for x in ws.gw_White_American_female_names] # if x in model]
    black_m = [x for x in ws.gw_Black_American_male_names] # if x in model]
    black_f = [x for x in ws.gw_Black_American_female_names] # if x in model]

    white = white_f + white_m
    black = black_f + black_m

    file.writelines(call(model, white_m, black_m, ws.gw_pos, ws.gw_neg, 'gw_blackWhite_male', lower_case=lower))
    file.writelines(call(model, white_f, black_m, ws.gw_pos, ws.gw_neg, 'gw_blackWhite_female', lower_case=lower))
    file.writelines(call(model, white, black, ws.gw_pos, ws.gw_neg, 'gw_blackWhite_MF', lower_case=lower))

    file.close()


########################################################################################################################
########################################################################################################################


def nosek(model, m_name, lower=False):
    """
    Conduct all WEAT comparisons of the nosek paper on the given model and save it in a text file in directory
    :param model:   Model to conduct the experiment
    :param m_name:  Model tag
    :return:        None
    """
    file = open('./OUT_weat/nosek/' + m_name + '#nosek.txt', 'w')

    pleasant_all = list(set(ws.Pleasant_1 + ws.Pleasant_2 + ws.Pleasant_3))
    unpleasant_all = ws.Unpleasant_1 + ws.Unpleasant_2 + ws.Unpleasant_3
    math = list(set(ws.Mathematics + ws.Mathematics_2 + ws.Science))
    arts = list(set(ws.Language + ws.Arts))

    # Math - attitude
    n_ma_1 = call(model, math, arts, pleasant_all, unpleasant_all, 'nosek_MAcombi_PosNegcombi', lower_case=lower)
    n_ma_2 = call(model, ws.Mathematics, ws.Arts, pleasant_all, unpleasant_all, 'nosek_MA_PosNegcombi', lower_case=lower)
    # Math -identity
    n_mi_1 = call(model, math, arts, ws.harvest_self, ws.harvest_other, 'nosek_MIcombi_SelfOther', lower_case=lower)
    n_mi_2 = call(model, ws.Mathematics, ws.Arts, ws.harvest_self, ws.harvest_other, 'nosek_MI_SelfOther', lower_case=lower)
    # Math-gender stereotype
    n_gs_1 = call(model, math, arts, ws.Masculine, ws.Feminine, 'nosek_GScombi_MF', lower_case=lower)
    n_gs_2 = call(model, ws.Mathematics, ws.Arts, ws.Masculine, ws.Feminine, 'nosek_GS_MF', lower_case=lower)

    for res in [n_ma_1, n_ma_2, n_mi_1, n_mi_2, n_gs_1, n_gs_2]:
        file.writelines(res)
    file.close()

    return False


def nosek_harvest(model, m_name, lower=False):
    """
    Conduct all WEAT comparisons of the nosek_harvest paper on the given model and save it in a text file in directory
    :param model:   Model to conduct the experiment
    :param m_name:  Model tag
    :return:        None
    """
    file = open('./OUT_weat/nosek_harvest/' + m_name + '#nosek_harvest.txt', 'w')
    # Race attitude
    file.writelines(call(model, ws.harvest_white, ws.harvest_black, ws.harvest_good, ws.harvest_bad, 'race', lower_case=lower))

    # Age attitude
    file.writelines(call(model, ws.harvest_young, ws.harvest_old,  ws.harvest_good, ws.harvest_bad, 'age', lower_case=lower))

    # (c) gender– career  stereotype,  measuring  the  association of male-female terms with career and family terms
    file.writelines(call(model, ws.harvest_m, ws.harvest_f, ws.harvest_career, ws.harvest_family, 'gendercareer_N', lower_case=lower))
    file.writelines(call(model, ws.harvest_mII, ws.harvest_fII, ws.harvest_career, ws.harvest_family,  'gendercareer_T', lower_case=lower))

    # (d) gender–science  stereotype,  measuring  the  association  of  male-female  terms with  science  and  liberal  arts  terms
    file.writelines(call(model, ws.harvest_m, ws.harvest_f, ws.harvest_science, ws.harvest_libArts, 'Science_N', lower_case=lower))
    file.writelines(call(model, ws.harvest_mII, ws.harvest_fII, ws.harvest_science, ws.harvest_libArts, 'Science_T', lower_case=lower))

    # (e) self-esteem,  measuring  attitudes  toward  self  versus other
    file.writelines(call(model, ws.harvest_self, ws.harvest_other, ws.harvest_good, ws.harvest_bad, 'selfEsteem', lower_case=lower))

    # (f) math–arts attitude;
    file.writelines(call(model, ws.harvest_arts, ws.harvest_math, ws.harvest_good, ws.harvest_bad, 'Math', lower_case=lower))
    file.writelines(call(model, ws.harvest_m, ws.harvest_f, ws.harvest_math, ws.harvest_arts, 'Math_N', lower_case=lower))
    file.writelines(call(model, ws.harvest_mII, ws.harvest_fII, ws.harvest_math, ws.harvest_arts, 'Math_T', lower_case=lower))

    file.close()


def monteith_pettit(model, m_name, lower=False):
    """
    Conduct all WEAT comparisons of the mp paper on the given model and save it in a text file in directory
    :param model:   Model to conduct the experiment
    :param m_name:  Model tag
    :return:        None
    """
    mp = open('./OUT_weat/mp/' + m_name + '#mp', 'w')

    depressed = ws.mp_depressed
    physic_ill = ws.mp_physic_ill

    permanent = ws.mp_permanent
    temp = ws.mp_temporary

    #depressed = [x for x in ws.mp_depressed if x in model]
    #physic_ill = [x for x in ws.mp_physic_ill if x in model]
    #delete = ['delete: '] + [x for x in ws.mp_depressed+ws.mp_physic_ill if x not in model]

    #permanent = [x for x in ws.mp_permanent if x in model]
    #temp = [x for x in ws.mp_temporary if x in model]

    #delete.extend(x for x in ws.mp_permanent if x not in model)
    #delete.extend(x for x in ws.mp_temporary if x not in model)

    #print(delete)
    #mp.writelines(delete)

    mp.writelines(call(model, depressed, physic_ill, permanent, temp, 'mp_stability', lower_case=lower))
    mp.writelines(call(model, depressed, physic_ill, ws.mp_controllable, ws.mp_uncontrollable, 'mp_controllability', lower_case=lower))
    mp.writelines(call(model, depressed, physic_ill, ws.mp_mental, ws.mp_physical, 'mp_etiology', lower_case=lower))
    mp.writelines(call(model, depressed, physic_ill, ws.mp_good, ws.mp_bad, 'mp_stability', lower_case=lower))

    mp.close()


def monteith_pettit_reverse(model, m_name, lower=False):
    """
    Conduct all WEAT comparisons of the mp paper on the given model and save it in a text file in directory
    :param model:   Model to conduct the experiment
    :param m_name:  Model tag
    :return:        None
    """
    mp = open('./OUT_weat/mp/' + m_name + '#mp', 'w')

    depressed = ws.mp_depressed
    physic_ill = ws.mp_physic_ill

    permanent = ws.mp_permanent
    temp = ws.mp_temporary

    mp.writelines(call(model,  permanent, temp, depressed, physic_ill, 'mpR_stability', lower_case=lower))
    mp.writelines(call(model,  ws.mp_controllable, ws.mp_uncontrollable, depressed, physic_ill,'mpR_controllability', lower_case=lower))
    mp.writelines(call(model, ws.mp_mental, ws.mp_physical, depressed, physic_ill, 'mpR_etiology', lower_case=lower))
    mp.writelines(call(model, ws.mp_good, ws.mp_bad, depressed, physic_ill, 'mpR_stability', lower_case=lower))

    mp.close()


good = ws.harvest_good + ws.mp_good + ws.gw_pos
bad = ws.harvest_bad + ws.mp_bad + ws.gw_neg

black = ws.harvest_black + ws.gw_Black_American_male_names + ws.gw_Black_American_female_names
white = ws.harvest_white + ws.gw_White_American_male_names + ws.gw_White_American_female_names


def do_all(model, m_name, lower=False):
    print('lower', lower)
    #greenwald(model, m_name, lower)
    #greenwald_black_white(model, m_name, lower)
    #greenwald_asian(model, m_name, lower)

    #nosek(model, m_name, lower)
    nosek_harvest(model, m_name, lower)

    #monteith_pettit(model, m_name, lower)
    os.system('spd-say "calculation finished"')


def exe_all_models():
  #  m = KeyedVectors.load_word2vec_format('./models/modelsGoogle/GoogleNews-vectors-negative300.bin', binary=True)
  #  do_all(m, 'Goo_stan', lower=False)
  #  logging.info('googleStan done')

  #  m = KeyedVectors.load_word2vec_format('./models/modelsGoogle/word2vec-slim/GoogleNews-vectors-negative300-SLIM.bin', binary=True)
  #  do_all(m, 'Goo_slim', lower=False)
  #  logging.info('googleSlim done')

    models = util.get_all_model_tags()
    CBOW = models[0]
    SG = models[1]

    for elem in CBOW:
        nosek_harvest(KeyedVectors.load(elem[1]), 'CB_' + elem[0], lower=True)
    for elem in SG:
        nosek_harvest(KeyedVectors.load(elem[1]), 'SG_' + elem[0], lower=True)

   # for elem in CBOW:
   #     do_all(KeyedVectors.load(elem[1]), 'CB_' + elem[0], lower=True)
   # for elem in SG:
   #     do_all(KeyedVectors.load(elem[1]), 'SG_' + elem[0], lower=True)



exe_all_models()
# nosek(KeyedVectors.load('./models/models/SG//Afr_sla_5'), 'TEST_Afr_sla_5', lower=True)

os.system('spd-say "calculation finished"')