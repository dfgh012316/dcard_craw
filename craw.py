import requests
from fake_useragent import UserAgent
import os.path
import json

def craw_dcard_article(id):
    user_agent = UserAgent()
    url = "https://www.dcard.tw/service/api/v2/posts/{}".format(id)
    dcard_json = requests.get(url, headers={
        "user-agent": user_agent.random}).json()

    return dcard_json


def gen_dcard_file(jsonfile):
    temp = {}
    temp['id'] = jsonfile['id']
    temp['forumAlias'] = jsonfile['forumAlias']
    temp['title'] = jsonfile['title']
    temp['gender'] = jsonfile['gender']
    temp['content'] = jsonfile['content']
    temp['topics'] = jsonfile['topics']
    temp['reactions'] = jsonfile['reactions']
    temp['createdAt'] = jsonfile['createdAt'].split("T")[0]
    temp['school'] = jsonfile['school']
    temp['totalCommentCount'] = jsonfile['totalCommentCount']

    def filter_reactions(reactions):
        for reaction in reactions:
            if reaction['id'] == '286f599c-f86a-4932-82f0-f5a06f1eca03':
                reaction['id'] = "like"
            elif reaction['id'] == '4b018f48-e184-445f-adf1-fc8e04ba09b9':
                reaction['id'] = "suprise"
            elif reaction['id'] == 'e8e6bc5d-41b0-4129-b134-97507523d7ff':
                reaction['id'] = "laugh"
            elif reaction['id'] == '011ead16-9b83-4729-9fde-c588920c6c2d':
                reaction['id'] = "orz"
            elif reaction['id'] == '514c2569-fd53-4d9d-a415-bf0f88e7329f':
                reaction['id'] = "cry"
            elif reaction['id'] == 'aa0d425f-d530-4478-9a77-fe3aedc79eea':
                reaction['id'] = "angry"
    filter_reactions(temp['reactions'])

    return temp


def write_to_file(data):
    filename = "-".join((data['forumAlias'], str(data['id']), data['createdAt'], ".json"))

    path = os.path.join(data['forumAlias'], filename)
    with open(path, 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
        
def craw_by_date(date_start, date_end, formAlias):
    # TODO
    # check fold exist
    # check the lastet article id
    return 0


def main():
    # TODO
    # Crawl data based on date range and kanban
    # craw_by_date(date_start, date_end, formAlias)
    dcard_article_rawdata = craw_dcard_article(238056760)
    dcard_article = gen_dcard_file(dcard_article_rawdata)
    write_to_file(dcard_article)


if __name__ == '__main__':
    main()
