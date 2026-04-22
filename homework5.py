class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"


class GlowStreamer(Streamer, Mutant):
    def ultimate_content(self):
        return self.live() + " | " + self.earn() + " | " + self.superpower()


class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return self.live() + " | " + self.viral() + " | " + self.superpower()


class DonateMage(Streamer, TikToker):
    def ultimate_content(self):
        return self.live() + " | " + self.earn() + " | " + self.viral()


print("GlowStreamer MRO:", GlowStreamer.mro())
print("ViralCyborg MRO:", ViralCyborg.mro())
print("DonateMage MRO:", DonateMage.mro())

print("\n--- LIVE TEST ---")
g = GlowStreamer()
v = ViralCyborg()
d = DonateMage()

print("GlowStreamer live:", g.live())
print("ViralCyborg live:", v.live())
print("DonateMage live:", d.live())

print("\n--- ULTIMATE CONTENT ---")
print(g.ultimate_content())
print(v.ultimate_content())
print(d.ultimate_content())
