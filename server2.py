import Pyro4

@Pyro4.expose
class StringConcatenator(object):
    def concatenate(self, s1, s2):
        return s1 + s2

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(StringConcatenator)
ns.register("example.concatenator", uri)

print("Server is ready.")
daemon.requestLoop()
