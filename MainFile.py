import httpimport

# url = "https://gist.githubusercontent.com/siddiqqulhakim/675179664d17fb34b4df07804be5f88b/raw/485af02828f152c0775bd16c8756a0973a6e9444"
# with httpimport.remote_repo(url):
#     import hello
# hello.abc()

with httpimport.github_repo('siddiqqulhakim', 'test', branch='master'):
    import test
test.say()