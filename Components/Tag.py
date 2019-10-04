from db_ops.ModelLayer import TagModel


class Tag:

    def add_tag(self, data):

        tag = TagModel()
        for key, value in data.items():
            tag.__setattr__(key, value)

        tag.insert()
        return {"success": True, "message": "Tag Added Successfully"}

    def get_tags(self, tag_name=None):
        tag = TagModel()
        if tag_name is not None:
            result = tag.fetch_by_tag_name(tag_name=tag_name)
        else:
            result = tag.fetch_all_tags()

        return result