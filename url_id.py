from twython import Twython

t = Twython(
    '{API key}',
    '{API key secret}',
)

class RetornaIdUrl:

    def retorna_url_img_pelo_id(self):
        user_profile = t.show_user(user_id=self)
        return str(user_profile['profile_image_url']).replace('normal', '400x400')

    def retorna_lista_id_by_user(self):
        x = t.get_friends_ids(screen_name=str(self))
        return list(x['ids'])
