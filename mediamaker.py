import os

not_used = [
{'title':"Mansion construction animation",

            'is_video':True,
            'filename':'mansion_super_super_small.avi',
            'video_point':120,
            'blockdropper':True,
         'date':'05/07/2020',
            },
{'title':"Desert temple construction",

            'is_video':False,
            'filename':'desert_temple_small.mp4',
            'video_point':28,
            'blockdropper':False,
         'date':'20/06/2020',
            },
{'title':"Amount of diamonds you CAN get out of a 300x300 area",

            'is_video':True,
            'filename':'diamonds_smaller.mp4',
            'video_point':10,
            'blockdropper':False,
         'date':'30/07/2020',
            },
{'title':"The amount of dia in a 500x500 area:",

            'is_video':True,
            'filename':'diamonds_small.mp4',
            'video_point':5,
            'blockdropper':False,
         'date':'01/06/2020',
            },
{'title':"Another fountain",

            'is_video':False,
            'filename':'fontein2.mp4',
            'video_point':5,
            'blockdropper':False,
         'date':'03/06/2020',
            },


]

posts = [
        {'title':"How to build an automatic chicken farm, short and animated",

         'is_video':True,
         'filename':'chickenfarm.mp4',
         'video_point':28,
         'blockdropper':True,
         'date':'05/09/2021',
         },
        {'title':"How to make a pumpkin melon farm, short and animated",

            'is_video':True,
            'filename':'melonfarm.mp4',
            'video_point':28,
            'blockdropper':True,
            'date':'12/08/2021',
            },
        {'title':"How to build an automatic sheep farm, short and animated",

            'is_video':True,
            'filename':'woolfarm.mp4',
            'video_point':28,
            'blockdropper':True,
         'date':'16/08/2021',
            },
        {'title':"Weaponsmith",

            'is_video':False,
            'filename':'weaponsmithbrighter.png',
            'video_point':28,
            'blockdropper':False,
         'date':'10/04/2021',
            },
        {'title':"-We got this on camera, mate! (render)",

            'is_video':False,
            'filename':'finaltheft.png',
            'video_point':28,
            'blockdropper':False,
         'date':'08/04/2021',
            },
        {'title':"When an iron golem looks into a mirror, he sees a much darker version of himself...",

            'is_video':False,
            'filename':'mirror_final.png',
            'video_point':28,
            'blockdropper':False,
         'date':'17/10/2020',
            },
        {'title':"An Axolotl I rendered, can't wait to see them in game!",

            'is_video':False,
            'filename':'final_axolotl_light.png',
            'video_point':28,
            'blockdropper':False,
         'date':'14/10/2020',
            },
        {'title':"All levels of Fortune compared",

            'is_video':True,
            'filename':'small_fortune.mp4',
            'video_point':35,
            'blockdropper':False,
         'date':'26/09/2020',
            },
        {'title':"Short animation I made. I hope you guys like it.",
            'is_video':True,
            'filename':'falling_small.mp4',
            'video_point':0,
            'blockdropper':False,
         'date':'19/09/2020',
            },
        {'title':"Amount of every block in a 100x100 basalt delta area",
            'is_video':True,
            'filename':'final_small_delta.mp4',
            'video_point':8,
            'blockdropper':False,
         'date':'25/08/2020',
            },
        {'title':"All pickaxes racing against each other.",

            'is_video':True,
            'filename':'final_small_mining.mp4',
            'video_point':0,
            'blockdropper':False,
         'date':'20/08/2020',
            },
        {'title':"Cuboctahedron",

            'is_video':False,
            'filename':'cuboctahedron.jpg',
            'video_point':28,
            'blockdropper':False,
         'date':'22/07/2020',
            },
        {'title':"The amount of each block in this 200x200 area visualized",

            'is_video':True,
            'filename':'final_sorted.mp4',
            'video_point':9,
            'blockdropper':False,
         'date':'11/08/2020',
            },
        {'title':"Well done son!",

            'is_video':False,
            'filename':'lavavallen_final.jpg',
            'video_point':28,
            'blockdropper':False,
         'date':'08/08/2020',
            },
        {'title':"The most loyal mob in minecraft",

            'is_video':False,
            'filename':'dog_saving.jpg',
            'video_point':28,
            'blockdropper':False,
         'date':'06/08/2020',
            },
    {'title':"A true hero",

            'is_video':False,
            'filename':'explosion_saving.jpg',
            'video_point':23,
            'blockdropper':False,
         'date':'03/08/2020',
            },
    {'title':"Amount of netherite in a 300x300 area visualized",

            'is_video':False,
            'filename':'netherite_high.mp4',
            'video_point':23,
            'blockdropper':False,
         'date':'01/08/2020',
            },
        {'title':"Dady?",

            'is_video':False,
            'filename':'plume_final.jpg',
            'video_point':28,
            'blockdropper':False,
         'date':'21/07/2020',
            },
    {'title':"Bonjour...",

            'is_video':False,
            'filename':'hello.jpg',
            'video_point':28,
            'blockdropper':False,
         'date':'19/07/2020',
            },
    {'title':"Well well well, look who we have here",

            'is_video':False,
            'filename':'final.jpg',
            'video_point':28,
            'blockdropper':False,
         'date':'09/07/2020',
            },
    {'title':"meow",

            'is_video':False,
            'filename':'miauw.jpg',
            'video_point':28,
            'blockdropper':False,
         'date':'08/07/2020',
            },
            {'title':"I made a little construction animation",
            'is_video':True,
            'filename':'small_construction.mp4',
            'video_point':20,
            'blockdropper':True,
         'date':'18/06/2020',
            },
    {'title':"If creepers had televisions",

            'is_video':False,
            'filename':'free_creeper_TV.png',
            'video_point':28,
            'blockdropper':False,
         'date':'16/06/2020',
            },
    {'title':"-Come on son, you can do this!",

            'is_video':False,
            'filename':'bright_skeletons.png',
            'video_point':28,
            'blockdropper':False,
         'date':'11/06/2020',
            },
    {'title':"There goes another here",

            'is_video':False,
            'filename':'drowning.png',
            'video_point':28,
            'blockdropper':False,
         'date':'09/06/2020',
            },
    {'title':"-What happened to grandpa? -Well... He got struck by lightning.",

            'is_video':False,
            'filename':'grandpa.png',
            'video_point':28,
            'blockdropper':False,
         'date':'08/06/2020',
            },
    {'title':"Please don't kill his mommy!",

            'is_video':False,
            'filename':'hatching.png',
            'video_point':28,
            'blockdropper':False,
         'date':'07/06/2020',
            },
    {'title':"The iron golems will be happy",
            'is_video':True,
            'filename':'outpost_destruction.mp4',
            'video_point':4,
            'blockdropper':False,
         'date':'06/06/2020',
            },
    {'title':"Soft marble race v2",

            'is_video':True,
            'filename':'neon_balletjes_small.mp4',
            'video_point':28,
            'blockdropper':False,
         'date':'02/05/2020',
            },
    {'title':"The most loyal mob in minecraft.",

            'is_video':False,
            'filename':'protect.png',
            'video_point':28,
            'blockdropper':False,
         'date':'04/06/2020',
            },
            {'title':"I tried to make a realistic fountain",

            'is_video':True,
            'filename':'fountain.mp4',
            'video_point':3,
            'blockdropper':False,
         'date':'30/05/2020',
            },
    {'title':"Just another iron golem farm",

            'is_video':False,
            'filename':'slavery.png',
            'video_point':28,
            'blockdropper':False,
         'date':'27/05/2020',
            },
    {'title':"Please someone help!",

            'is_video':False,
            'filename':'iron_golem_hanging.png',
            'video_point':28,
            'blockdropper':False,
         'date':'26/05/2020',
            },
    {'title':"A typical minecraft scene",

            'is_video':False,
            'filename':'active_wandering_trader.png',
            'video_point':28,
            'blockdropper':False,
         'date':'25/05/2020',
            },
    {'title':"That he may rest in peace.",

            'is_video':False,
            'filename':'attack.png',
            'video_point':28,
            'blockdropper':False,
         'date':'22/05/2021',
            },
    {'title':"I made lava a little better.",

            'is_video':True,
            'filename':'lavafall.mp4',
            'video_point':7,
            'blockdropper':False,
         'date':'18/05/2020',
            },
    {'title':"Where they belong...",

            'is_video':False,
            'filename':'final_library.png',
            'video_point':28,
            'blockdropper':False,
         'date':'19/05/2020',
            },
    {'title':"Sand explosion!",

            'is_video':True,
            'filename':'sand_fall.mp4',
            'video_point':4,
            'blockdropper':False,
         'date':'17/05/2020',
            },
    {'title':"My take on realistic minecraft fluids",

            'is_video':True,
            'filename':'final.mp4',
            'video_point':3,
            'blockdropper':False,
         'date':'15/05/2020',
            }
    ]


def generatemedia():
    for post in posts:
        filename = post['filename']
        name = filename.split('.')[0]
        if post['is_video']:
            os.system(f"ffmpeg -ss {post['video_point']} -i {'raw/' + filename} -vf scale=1920:1080 -vframes 1 -f image2 {'images/' + name + '_big.jpg'} -y")
            os.system(f"ffmpeg -ss {post['video_point']} -i {'raw/' + filename} -vf scale=320:180 -vframes 1 -f image2 {'images/' + name + '_small.jpg'} -y")
            os.system(f"cp {'raw/' + filename} {'videos/' + filename}")
        else:
            os.system(f"ffmpeg -i {'raw/' + filename} -vf scale=1920:1080 -f image2 {'images/' + name + '_big.jpg'} -y")
            os.system(f"ffmpeg -i {'raw/' + filename} -vf scale=320:180 -f image2 {'images/' + name + '_small.jpg'} -y")
    




if __name__ == "__main__":
    generatemedia()
