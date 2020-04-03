
########################################################################################################################
''' established in literature '''
########################################################################################################################
# Greenwald
gw_pos = ['caress', 'freedom', 'health', 'love', 'peace', 'cheer', 'friend', 'heaven', 'loyal', 'pleasure',
          'diamond', 'gentle', 'honest', 'lucky', 'rainbow', 'diploma', 'gift', 'honor', 'miracle', 'sunrise',
          'family', 'happy', 'laughter', 'paradise', 'vacation']

gw_neg = ('abuse crash filth murder sickness accident death grief poison stink assault disaster hatred pollute '
                  'tragedy bomb divorce jail poverty ugly cancer evil kill rotten vomit agony prison ').split()

gw_flow = ('aster clover hyacinth marigold poppy azalea crocus iris orchid rose bluebell daffodil lilac '
           'pansy tulip buttercup daisy lily peony violet carnation gladiola magnolia petunia zinnia').split()

gw_insec = ('ant caterpillar flea locust spider bedbug centipede fly maggot tarantula bee cockroach gnat '
           'mosquito termite beetle cricket hornet moth wasp blackfly dragonfly horsefly roach weevil').split()

gw_instr = ('bagpipe cello guitar lute trombone banjo clarinet harmonica mandolin trumpet bassoon drum '
            'harp oboe tuba bell fiddle harpsichord piano viola bongo flute horn saxophone violin').split()

gw_weapon = ('arrow club gun missile spear ax dagger harpoon pistol sword blade dynamite hatchet rifle '
           'tank bomb firearm knife shotgun teargas cannon grenade mace slingshot whip').split()

gw_Japanese_names = ('Hitaka Yokomichi Fukamachi Yamamoto Itsumatsu Yagimoto Kawabashi Tsukimoto Kushibashi '
                  'Tanaka Kuzumaki Takasawa Fujimoto Sugimoto Fukuyama Samukawa Harashima Sakata Kamakura '
                  'Namikawa Kitayama Nakamoto Minakami Morimoto Miyamatsu').split()

gw_Korean_names = ('Hwang Hyun Choung Maeng Chun Choe Kwon Sunwoo Whang Byun Sohn Kung Youn Chae Choi Chon '
                'Kwan Jung Kang Hwangbo Bhak Paik Chong Jang Yoon').split()

gw_Truncated_Japanese_names = ('Hitak Yoko Fukama Yamam Itsu Yagi Kawa Tsukim Kushi Tana Kuzu Taka Fuji Sugi '
                            'Fuku Samu Hara Saka Kama Namikaw Kita Naka Minak Mori Miya').split()

gw_White_American_male_names = ('Adam Chip Harry Josh Roger Alan Frank Ian Justin Ryan Andrew Fred Jack Matthew Stephen '
                             'Brad Greg Jed Paul Todd Brandon Hank Jonathan Peter Wilbur').split()

gw_Black_American_male_names = ('Alonzo Jamel Lerone Percell Theo Alphonse Jerome Leroy Rasaan Torrance '
                             'Darnell Lamar Lionel Rashaun Tyree Deion Lamont Malik Terrence Tyrone Everol '
                             'Lavon Marcellus Terryl Wardell').split()

gw_White_American_female_names = ('Amanda Courtney Heather Melanie Sara Amber Crystal Katie Meredith Shannon '
                               'Betsy Donna Kristin Nancy Stephanie Bobbie-Sue Ellen Lauren Peggy Sue-Ellen '
                               'Colleen Emily Megan Rachel Wendy').split()

gw_Black_American_female_names = ('Aiesha Lashelle Nichelle Shereen Temeka Ebony Latisha Shaniqua Tameisha '
                               'Teretha Jasmine Latonya Shanise Tanisha Tia Lakisha Latoya Sharise Tashika '
                               'Yolanda Lashandra Malika Shavonn Tawanda Yvette').split()


# European-American vs. African-American names
European_American = gw_White_American_female_names + gw_White_American_male_names
African_American = gw_Black_American_female_names + gw_Black_American_male_names
# Male vs. Female names
Male_Names = gw_Black_American_male_names + gw_White_American_male_names
Female_Names = gw_Black_American_female_names + gw_White_American_female_names


##################################################
# (10) Nosek, Banaji, Greenwald: Math, male, me, female

Pleasant_1      =   'assertive athletic strong compassion support sympathetic laughter champion paradise vacation'.split()
Unpleasant_1    =   'brutal destroy ruthless confusion insecure naive bad poor waste crude'.split()

Pleasant_2      =   'ambition cuddle excitement glory joy love paradise pleasure romantic miracle'.split()
Unpleasant_2    =   'agony death detest disaster humiliate jealousy punishment stress tragedy war'.split()

Pleasant_3      =   'affectionate cozy enjoyment friend hug laughter passion peace snuggle triumph'.split()
Unpleasant_3    =   'afraid crucify despise failure hatred irritate nightmare slap terrible violent'.split()

#Mathematics/Language (preliminary study and Study 1)
Mathematics     =   'algebra formula geometry equation subtract variable add square multiply numbers'.split()
Language        =   'English grammar words sentence adjective poetry verbs pronoun paragraph letters'.split()

Science         =   'science technology physics chemistry Einstein NASA experiment astronomy'.split()
Arts            =   'poetry art Shakespeare dance literature novel symphony drama'.split()

Mathematics_2   =   'math algebra geometry calculus equations computation numbers Newton'.split()

#I/They (Studies 1 and 2)
#I: I, me, myself, mine
#They: they, them, their, theirs
Masculine       =   'brother father uncle grandfather son he his him'.split()
Feminine        =   'sister mother aunt grandmother daughter she hers her'.split()


### from source (9) nosek harvest ###
# Gender-Career stereotype
harvest_m = ('John Paul Mike Kevin Steve Greg Jeff Bill').split()
harvest_f = ('Amy Joan Lisa Sarah Diana Kate Ann Donna').split()
harvest_career= ('Executive Management Professional Corporation Salary Office Business Career').split()
harvest_family = ('Home Parents Children Family Cousins Marriage Wedding Relatives').split()

# Gender-Science stereotype
harvest_mII = ('Male Man Boy Brother He Him His Son').split()
harvest_fII = ('Female Woman Girl Sister She Her Hers Daughter').split()
harvest_science = ('Chemistry Physics Biology Biophysics Engineering Astronomy Biochemistry Neuroscience').split()
harvest_libArts = ('Philosophy Arts Humanities History Spanish English Latin Music').split()

# math attitude
harvest_math = ('Math Algebra Geometry Calculus Equations Computation Numbers Addition').split()
harvest_arts = ('Poetry Art Dance Literature Novel Symphony Drama Sculpture').split()

# age attitude
harvest_old = ('Ethel Bernice Gertrude Agnes Cecil Wilbert Mortimer Edgar').split()
harvest_young = ('Tiffany Michelle Cindy Kristy Brad Eric Joey Billy').split()

# race attitude
harvest_black = ('Tyrone Malik Jamal Leroy Temeka Latisha Tawanda Shaniqua').split()
harvest_white = ('Chip Brad Walter Ralph Heather Betsy Peggy Colleen').split()

# self esteem
harvest_self = ['I', 'mine', 'me', 'myself']
harvest_other = ['they', 'them', 'their', 'theirs']

harvest_good = ('Joy Love Peace Wonderful Pleasure Friend Laughter Happy').lower().split()
harvest_bad = ('Agony Terrible Horrible Nasty Evil War Awful Failure Death').lower().split()


### from Monteith pettit (23) - depression
# todo: was ist mit den Begriffen aus mehereren einzelworten?
mp_depressed = ('sad hopeless gloomy tearful miserable depressed').split()
mp_physic_ill = ('sick illness influenza disease virus cancer').split()

mp_permanent = ('stable always constant persistent chronic prolonged forever').split()
mp_temporary = ('impermanent unstable variable fleeting short-term brief occasional').split()

mp_controllable = ('avoidable preventable guilty fault manageable blameworthy').split()
mp_uncontrollable = ('unavoidable inevitable innocent faultless unmanageable blameless').split()

mp_mental = ('stress trauma mental cognitive learned acquired helplessness coping life_event ').split()   # style
mp_physical = ('genes chemical physiology brain physical inherited hereditary hormones neurotransmitter').split() #

mp_good = ('positive pleasant enjoy glorious wonderful bliss').split()
mp_bad = ('negative horrible agony terrible unpleasant despise').split()


sets = []
f = open('foo.txt', 'w')
for s in sets:
    s.sort()
    for w in s:
        f.write(str(w) + ', ')
    f.write('\n\n')
f.close()

generalPos = set(Pleasant_1 + Pleasant_2 + Pleasant_3           + gw_pos + harvest_good + mp_good)
generalNeg = set(Unpleasant_1 + Unpleasant_2 + Unpleasant_3     + gw_neg + harvest_bad + mp_bad)
########################################################################################################################
''' manually generated '''
########################################################################################################################
#TODO: Überarbeiten und im Dokument einpflegen

# own target & attribute sets:
a1_1 = ['always', 'ought', 'should', 'shall', 'desired']
a2_1 = ['not', 'never', 'no', "don't", "shouldn't", 'forbidden']
#file.writelines(call(t1_1, t2_1, a1_1, a2_1, 'own: verb'))

t1_2 = ['respectful', 'honest', 'kind', 'fair']
t2_2 = ['envious', 'greedy', 'evil', 'corrupt']

a1_2 = ['be', 'good', 'are']
a2_2 = ['not', "don't", 'never', 'bad']
#file.writelines(call(t1_2, t2_2, a1_2, a2_2, 'own: adj'))


### bible stuff
lord = ('lord god grace mercy glory prayer sign blessing praise righteousness').split()
sin = ('sin wrong evil punishment hate curse desire shame guilt pride').split()


#### law stuff
guilty = ['jail', 'prison', 'guilty', 'imprison', 'imprisoned', 'conviction']
innocent = ['innocent', 'acquittal', 'righteous', 'righteously', 'honest', 'honestly']


### Do Dont
do_quantifier = ['always', 'often', 'frequently', 'usually', 'commonly', 'consistently']
dont_quantifier = ['never', 'not', 'seldom', 'uncommonly', 'unusually', 'exceptionally']

do_hilfsverben = ['should', 'do', 'ought', 'shall']
dont_hilfsverben = ['should_not', 'do_not', "don't", "shouldn't", 'ought_not', 'shall_not', "shan't"]



### religion
Hindi_dict = {'Vedas':   'sacred texts of Hinduism',
              'Upanishads':   'Philosophical texts',
              'Gita':         'Sacred scripture',
              'Ramayana':     'Hindu epic',
              'Atman':        'Soul, ones true self',
              'Avatar':       'deliberate descent of a deity',
              'Bhajans':      'devotional song',
              'Brahman':      'eternal and unchanging divine reality',
              'Trimurti':     'Idea of personification of cosmic functions',
              'Brahma':       'God of creation',
              'Vishnu':       'God who contorls the universe',
              'Shiva':        'God of destruction',
              'Darshan':      'Sight of diety that brings blessing',
              'Guna':         'State of mind',
              'Guru':         'Teacher',
              'Krishna':      'Avatar of Vishnu',
              'Rita':         'determinded natural law',
              'Akriti':       'Idea that truth comes from beyond the human constraints of space and time',
              'Karma':        'all deeds have consequences',
              'Maya':         'allusion of the physical world, which one needs to see through in order to '
                              'be reunited with Brahaman',
              'Moksha':       'elease from Samsara and from the physical world',
              'Murt':         'physical representation of a deity',
              'Puja':         'ritual that acts as an offering to various deities',
              'Samsara':      'life is a continuous flow and does not end with death',
              'Shruti':       'Literature, considered to come from divine revelation',
              'Smriti':       'Part of sacret literature',
              'Varna':        'division of Hindus into four classes',
              'Jati':         'caste, meaning a one’s existence determined at birth',
              'Yoga':         'means Union'}


Islam_dict = {'Adhan':          'The call to prayer.',
              'Allah':          'The Arabic term for God.',
              'Ayatollah':      'A Shiite',
              'alaikum':        'As-salaam ...; A common greeting',
              'Ayah':           'A verse in the Qur’an.',
              'Fatihah':        'First chapter of the Qur’an.',
              'Fatwa':          'Leading ruling within islam',
              'Fitr':           'Eid ul ...; Celebration at the end of Ramadan.',
              'Adha':           'Eid ul ...; Celebration at the end of Hajj.',
              'pillars':        '5 central practices of Muslims to help establish a spiritual relationship with God.',
              'Hadith':         'Sayings of the Prophet Muhammad.',
              'Hajj':           'pilgrimage to Mecca; one of the Five Pillars of Islam.',
              'Hijab':          'Headscarf worn by Muslim women for modesty.',
              'Hijrah':         'Muhammads flight from Mecca to Medina in A',
              'Ihsan':          'Arabic term which means moral excellence.',
              'Imam':           'The leader of congregational prayer, or a religious leader.',
              'Islam':          'The proper name of the religion.',
              'Kabah':          'Building in Mecca.',
              'Mecca':          'the holiest city of Islam; Muhammads birthplace',
              'madrasas':       'Islamic schools',
              'Masjid':         'The Arabic word for mosque.',
              'mosque':         'house of worship where Muslims gather for communal prayers.',
              'Monotheism':     'The belief in one God.',
              'Muhammad':       'The final prophet to whom Muslims believe God revealed the Qur’an.',
              'Muslim':         'A person who follows the religion of Islam.',
              'Prophet':        'A person Muslims believe was chosen by God to teach.',
              'Koran':          'The Holy Book of Islam.”',
              'Sunnah':         'Example or practice of the Prophet Muhammad.',
              'Surah':          'A chapter of the Qur’an.'}


Jew_dict ={
    'Adar':         'Twelfth month of jewish year',
#    'Adoshem':      'substitute for a name of God',
#    'Agunah':       'Literally, anchored.  A woman whose husband disappeared without divorcing her.',
    'Amidah':       'Literally, standing.  A prayer that is the center of any Jewish religious service.',
#    'Aninut':       'The period of mourning between the time of death and the time of burial.',
    'Asham':        'A guilt offering.',
    'Av':           'The fifth month of the Jewish year',
#    'Avelut':       'The period of mourning after the burial of a parent, child, sibling, or spouse.',
    'beit':         'house, word occurs in different jewish terms',
#    'Bentsch':      'Blessing',
#    'Berakhah':     'Blessing',
    'Dati':         'The Hebrew word for religious Jews, used in Israel.',
#    'Elokeynu':     'A substitute for a name of God',
    'Mitzvah':      'Bar ... or bat ...; ceremony',
    'Aliyah':       'Literally, ascension. Reading from the Torah or Emigrating to Israel ',
    'Chutzpah':     'Brazen arrogance, guts, presumption, or gall (positive trait)',
    'Iyar':         'The second month of the Jewish year,',
#    'Kippah':       'hat that Jewish men wear',
    'yarmulke':     'ohter word for Kippah',
    'Kosher':       'Correct, proper',
#    'chayim':       'Literally “To life!” Said like “Cheers!” when drinking a toast',
    'Mazel':        '... Tov. Good luck!',
    'Shalom':       'Hello, goodbye, or peace.',
    'Tikkun':       '... olam; The healing of the world.',
    'Torah':        'The first five books of the Hebrew Bible, hand - written on a scroll of parchment',
} # see https://www.mechon-mamre.org/jewfaq/glossary.htm for more


Buddhism_dict = { # http://webspace.ship.edu/cgboer/buddhavocab.html
    # Abhidharma pitaka -- higher teachings, philosophy
    # Alaya-vijñana -- “store” consciousness (similar to collective unconscious?)
    'Amitabha':     'the Buddha of the Western “Pure Land." Also known as Amida.',
    'Ananda':       "Buddha’s friend, cousin, and favorite disciple, and the monk who remembered the Sutras.",
    #'Anatman':      'not-self, self or ego not ultimately real.',
    #'Annitya':      'change, impermanence of all things, including us.',
    #'Arahant':      'Worthy one, a name for the Buddha.',
    #'Arhat':        'a monk who has achieved nirvana.',
    'Asanga':       "one of two brothers who lived in India in the 300's ad who developed Yogachara.",
    'Asita':        "the astrologer who predicts Buddha’s fate",
    'Asuras':       "titans or demigods.",
    #'Avalokiteshwara': "boddhisattva of compassion",
    #'Avidya ':      '(avijja) -- ignorance, delusion.',
    'Bardo':        "(Tibet) the period between death and rebirth.",
    #'Bhagava':      "The blessed one, a name for the Buddha.",
    'Bhikshu':      'monk.',
    #'Bhikshuni':    'nun.',
    #Bodh-gaya -- a town in Bihar where Buddha was enlightened at 35.
    'Bodhi':        'enlightenment, awakening.',
    #Bodhi tree -- the fig tree under which Buddha gained enlightenment.
   # 'Bodhicitta':   'sanskrit word for mind of enlightenment',
    'Bodhidharma':  'monk who brought Buddhism to China.',
    'Bodhisattva':  'enlightened being who remains in this existence to help others, a saint.',
    'Brahma':       'the supreme deva, who convinced Buddha to teach.',
    #Brahma vihara -- four "sublime states" of the boddhisattva: Maitri, Karuna, Mudita, Upeksa.
    'Buddha':       'The awakened one, the enlightened one.',
    #Ch’an -- Chinese for Zen Buddhism.
    'Chandaka':     'Buddha’s squire, who helped him leave his princely life.',
    #Ching-T’u -- Chinese for Pure Land.
    'Citta':        'basic mind or consciousness',
    #Citta-matra -- mind only, idealism
    #Dalai Lama -- the leader of Tibetan Buddhists.
    #Deer Park -- where Buddha gave his first sermon, in Sarnath, near Benares, to the five sadhus.
    #Dependent origination -- “one thing leads to another,”  all is connected.
    # 'Devadatta':    'Buddha’s evil cousin. Theodore.',
    'Devas':        'gods.',
    'Dhamma':       'Pali for dharma.',
    'Dharma':       '(dhamma) --  the teachings of the Buddha.',
   # 'Dharmakaya':   'Buddha-mind, the pervasive essence',
    #'Dharmas':      'ultimate elements of the universe (not dharma as in teachings!)',
    'Dhyana':       'meditation.',
    'Dogen':        '(1200-1253) -- monk who brought Soto Zen to Japan.',
    #'Duhkha':       '(dukkha) -- suffering, distress, lack of peace.  First noble truth.',
    'Dzogchen':     'Tibetan tantric techniques for rapid enlightenment.',
  #  'Dvesha':       '(dosha) -- hatred, anger, avoidance.',
    #Eightfold Path -- right view, aspiration, speech, action, livelihood, effort, mindfulness, concentration.
    #Five sadhus -- the five ascetics who practiced self-mortification with the Buddha.
    #Flower Adornment School -- a sect which attempted to consolidate all forms of Buddhism.  Also known as Hua-Yen or Kegon.
    #'Gandharvas':   'angelic beings who provide the gods with music.',
    'Gati':         'realm.  Used to refer to the six realms (gods, titans, humans, animals, ghosts, and demons)',
    'Gautama':      '(Gotama) -- Buddhas family name.',
   # 'Hinayana':     'southern Buddhism (“small or lesser vehicle or journey”).',
    'Indra':        'a major deva, originally the Hindu sky god.',
    'Jodo':         'Jodoshin -- Japanese for Pure Land.',
    #'Jodoshin':     'Japanese for Pure Land.',
    'Kalpa':        'millions of years, an eternity.',
    'Kamma':        'Pali for karma.',
    'Kapilavastu':  'Shakyan capital, where Buddha grew up.',
    'Karma':        'intentional or willed act.',
    'Karuna':       'compassion or mercy, the special kindness shown to those who suffer. One of the four brahma vihara.',
    #'Kashinagara':  'were Buddha died (near Lumbini), in a grove of sala trees.',
    'Koan':         'a very brief story demonstrating the paradoxical nature of dualistic thinking.  Used in Zen meditation.',
    #Kwan Yin , Kwannon -- Chinese and Japanese names for Avalokiteswara.
    #Lama -- Tibetan tantric master, now often used to refer to any respected monk.
    #Lumbini Grove -- where Buddha was born, during his mother’s trip to her parents home.
  #  'Madhyamaka':   'middle way, negative logic, not this -- not that',
    #'Mahakyashapa': 'the monk who understood the silent sermon and led the first council.',
    'Mahamaya':     'or Mayadevi -- Buddha’s mother, who died seven days after his birth',
   # 'Mahaprajapati':'Buddha’s aunt and stepmother, founder of Buddhist nuns.',
    'Mahayana':     'northern Buddhism (“large or greater vehicle or journey”).',
    'Maitreya':     'the future Buddha, who will be born 30,000 years from now.',
    'Maitri':       'caring, loving kindness displayed to all you meet.  One of the four brahma   vihara.',
    'Manas':        'I-consciousness, mind, intelligence.',
    'Mandala':      'a complex, circular, symmetrical image used in meditation',
    'Mantra':       'a phrase or syllable repeated during meditation',
    'Mara':         'a deva associated with death and hindrances to enlightenment. It was Mara who tempted Buddha under the bodhi tree.',
    'Marga':        'the path, track.  The eightfold noble path.  Fourth noble truth.',
    'Metta':        'Pali for Maitri.',
    #'Mudita':       'sympathetic joy, being happy for others, without a trace of envy.  One of the four brahma vihara.',
    'Mudra':        'symbolic hand positions',
    'Nagarjuna':    'monk who developed Madhyamaka in India about 150 ad.',
    'Nagas':        'great serpents (or dragons, or water creatures). The king of the Nagas protected Buddha from a storm.',
    'Nibbana':      'Pali for nirvana.',
    'Nichiren':     'Japanese school popular in west, and the name of its founder.  Emphasizes chanting.',
    #'Nirmankaya':   'Gotama, the historical Buddha.',
    #'Nirodha':      'containment of suffering.  Third noble truth.',
    'Nirvana':      'liberation, enlightenment, release from samsara.',
    'Pali':         'a language related to Sanskrit in which the earliest scriptures were recorded in Sri Lanka.',
    #Pali canon -- see the Tripitaka.
    #Pancha shila -- five moral precepts:  Avoid killing, or harming any living thing;  Avoid stealing; Avoid sexual irresponsibility;  Avoid lying, or any hurtful speech;  Avoid alcohol and drugs which diminish clarity of consciousness.
    'Panna':        'Pali for prajña',
    #'Pitaka':       'basket, referring to the Tripitaka or scriptures.',
    'Prajna':       '(pañña) -- wisdom.',
   # 'Prajnaparamita': 'a massive collection of Mahayana texts, including the Heart and Diamond Sutras.',
   # Prateyaka-buddha -- solitary realizer.
    'Preta':       'hungry ghosts.',
    'Puja':         'ceremony in which offerings and other acts of devotion are performed.',
  #  'Pu-tai':       'the laughing buddha, chinese monk, incarnation of Maitreya',
    'Rahula':       'Buddha’s son.',
    #Rinzai Zen -- a Zen sect that makes extensive use of koans.
    'Rupa':         'form, the physical body and senses',
    'Samadhi':      'meditation.',
    'Samatha':      'Pali for Shamatha.',
    #'Sambhogakaya': 'Buddha as a deva or god.',
    #'Samjna':       'perception',
    'Samsara':      'the wheel of cyclic existence, birth-life-suffering-death-rebirth...',
    'Samskara':     'mental formations (emotions and impulses)',
    'Samudaya':     'arising or root of suffering.  Second noble truth.',
    'Sangha':       'the community of monks and nuns.',
    'Sanskrit':     'an early language of northern India, modified and used as a religious language by some Buddhists.',
    #'Sanzen':       'interview with a master in Zen Buddhism',
    'Sati':         'Pali for smrti.',
    'Satori':       'Zen term for enlightenment.',
    'Shakyamuni':   'Sage of the Sakyas, a name for the Buddha.',
    #'Shakyas':      'a noble clan, ruled an area of southern Nepal.',
    #'Shikantaza':   'mindfulness meditation in Zen Buddhism.',
    'Shila':        '-- morality.',
    #'Shravaka':     'hearer,” one who needs the help of others to become enlightened.',
    #Shrota-appana -- “stream-winner” (only seven more rebirths!).
#    'Shuddodana':    'Buddha’s father.',
    #'Shunyata':     'emptiness, lack of inherent existence of “own nature.”',
    #Siddhartha Gautama -- “He who has reached his goal.”
    'Sila':         'Pali for shila.',
    #Six realms -- realms of the gods, asuras, humans, animals, pretas, narakas.
    #'Skandhas':     'parts of the self.',
    #'Smrti':        ' (sati) -- mindfulness, meditation.',
    #Soto Zen -- A Zen sect emphasizing Shikantaza meditation
    #'Sthaviravada': 'Sanskrit for Theravada, "way of the elders"',
    'Sujata':       'the village girl who gave Buddha milk-rice.',
    #'Sukhavati':    'Sanskrit for Blissful Land, the "Pure Land" of Amitabha.',
    'Sutra':        'pitaka -- sacred texts, sayings of the Buddha.',
    'Tantra':       'yogic, magico-ritual form.',
    'Taras':        'a set of 21 female saviors, born from Avalokiteshwara’s tears.  Green Tara and   White Tara are the best known.',
    'Tathagata':    '“thus gone,” a name for the Buddha.',
    'Tendai':       'see White Lotus School.',
    'Thangka':      'a traditional Tibetan painting of a holy being.',
    'Theravada':    'way of the elders,” only surviving form of southern Buddhism.',
    #'Tipitaka':     'Pali for Tripitaka.',
    'Tripitaka':    '(three baskets) -- earliest Buddhist scriptures:  Vinaya pitaka, sutra pitaka,   abhidarma pitaka.',
    'Trishna':      '(tanha) -- thirst, craving, desire.',
    'Upali':        'the first person ordained as a monk by the Buddha, a barber, and the monk who  remembered the Vinaya or code of the monks.',
    #'Upeksa':       '(upekkha) is equanimity, levelness, or grace.  One of the four brahma vihara.',
    'Vajrayana':    'tantric Buddhism (“thunderbolt vehicle”), esp. Tibetan Buddhism.',
   #'Vasubandhu':   'one of two brothers who lived in India in the 300s ad who developed   Yogachara.',
    #'Vedana':       'sensation, feeling.',
    'Vijnana':      'consciousness or mind.',
    #Vinaya pitaka -- discipline basket (code of behavior for monks).
  #  'Vipaka':       '“fruit” of willed act, the consequences.',
   # 'Vipashyana':   '(vipassana) -- insight, mindfulness.',
    'Yama':         'the king of the 21 hells.',
    'Yashodhara':   'Buddha’s wife, whom he married when they were both 16',
    #'Yidam':        'mental image of a god or other entity used for meditation',
    #'Yogacara':     '(or vijñañavada) -- school emphasizing primacy of consciousness',
    'Zazen':        'sitting meditation in Zen Buddhism',
    'Zen':          'a group of Buddhist sects that focus on meditation.  Also known as Chan, Son, or Dhyana.'
}


hindi_list = list(Hindi_dict.keys())
jew_list = list(Jew_dict.keys())
islam_list = list(Islam_dict.keys())
buddhism_list = list(Buddhism_dict.keys())


########################################################################################################################
''' computationally generated '''
########################################################################################################################

### AFINN
AFINN_pos_strict = ['hurrah', 'superb', 'thrilled', 'outstanding', 'breathtaking']
AFINN_neg_strict = ['motherfucker', 'motherfucking', 'cunt', 'nigger', 'cock', 'bastard', 'niggas', 'bitches', 'prick',
                    'slut', 'twat', 'bastards', 'son-of-a-bitch', 'cocksuckers', 'bitch', 'cocksucker']

AFINN_pos_extenuated = ['roflmao', 'triumphant', 'fun', 'wowww', 'rejoice', 'ecstatic', 'overjoyed', 'roflcopter',
                        'rejoices', 'rotflol', 'miracle', 'winning', 'lmfao', 'masterpiece', 'terrific', 'godsend',
                        'rofl', 'rotfl', 'woow', 'wowow', 'rotflmfao', 'exuberant', 'fabulous', 'fantastic', 'euphoric',
                        'rapturous', 'win', 'awesome', 'lmao', 'lifesaver', 'triumph', 'winner', 'wonderful',
                        'rejoicing', 'heavenly', 'masterpieces', 'rejoiced', 'brilliant', 'wins', 'wow', 'stunning',
                        'wooo', 'funny', 'funnier', 'amazing']
AFINN_neg_extenuated = ['frauds', 'fuckhead', 'shit', 'torture', 'jackass', 'torturing', 'shrew', 'fucker', 'scumbag',
                        'bullshit', 'damn', 'shithead', 'catastrophic', 'fuckers', 'damnit', 'rape', 'hell', 'pissed',
                        'fraudster', 'wtf', 'ass', 'dick', 'tortured', 'fraudsters', 'fuck', 'whore', 'fuckface',
                        'fucktard', 'dickhead', 'fuked', 'fucking', 'rapist', 'fraudulence', 'assfucking', 'jackasses',
                        'damned', 'fuking', 'piss', 'asshole', 'fraud', 'fraudulent', 'fucked', 'tortures']


AFINN_pos_large = ['outstanding', 'roflmao', 'triumphant', 'fun', 'wowww', 'rejoice', 'ecstatic', 'overjoyed',
                   'roflcopter', 'rejoices', 'rotflol', 'miracle', 'winning', 'lmfao', 'masterpiece', 'terrific',
                   'godsend', 'rofl', 'rotfl', 'thrilled', 'woow', 'wowow', 'rotflmfao', 'exuberant', 'fabulous',
                   'fantastic', 'euphoric', 'rapturous', 'win', 'awesome', 'breathtaking', 'superb', 'lmao', 'lifesaver',
                   'triumph', 'winner', 'wonderful', 'rejoicing', 'heavenly', 'masterpieces', 'rejoiced', 'brilliant',
                   'wins', 'wow', 'hurrah', 'stunning', 'wooo', 'funny', 'funnier', 'amazing']
AFINN_neg_large = ['frauds', 'fuckhead', 'shit', 'torture', 'jackass', 'torturing', 'shrew', 'niggas', 'fucker',
                   'scumbag', 'bullshit', 'bitch', 'damn', 'shithead', 'catastrophic', 'fuckers', 'damnit', 'slut',
                   'rape', 'hell', 'pissed', 'fraudster', 'wtf', 'cocksuckers', 'ass', 'motherfucker', 'cock', 'dick',
                   'tortured', 'nigger', 'fraudsters', 'fuck', 'cocksucker', 'whore', 'fuckface', 'fucktard',
                   'dickhead', 'twat', 'bastards', 'fuked', 'bitches', 'motherfucking', 'fucking', 'cunt', 'rapist',
                   'fraudulence', 'assfucking', 'jackasses', 'damned', 'fuking', 'piss', 'asshole', 'prick', 'fraud',
                   'fraudulent', 'fucked', 'son-of-a-bitch', 'bastard', 'tortures']


########################################################################################################################