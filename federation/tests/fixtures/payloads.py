# -*- coding: utf-8 -*-

ENCRYPTED_DIASPORA_PAYLOAD = """<?xml version='1.0'?>
            <diaspora xmlns="https://joindiaspora.com/protocol" xmlns:me="http://salmon-protocol.org/ns/magic-env">
                <encrypted_header>{encrypted_header}</encrypted_header>
                <me:env>
                    <me:data type='application/xml'>{data}</me:data>
                    <me:encoding>base64url</me:encoding>
                    <me:alg>RSA-SHA256</me:alg>
                    <me:sig>{signature}</me:sig>
                </me:env>
            </diaspora>
        """


UNENCRYPTED_DIASPORA_PAYLOAD = """<?xml version='1.0'?>
            <diaspora xmlns="https://joindiaspora.com/protocol" xmlns:me="http://salmon-protocol.org/ns/magic-env">
                <header>
                    <author_id>bob@example.com</author_id>
                </header>
                <me:env>
                    <me:data type='application/xml'>{data}</me:data>
                    <me:encoding>base64url</me:encoding>
                    <me:alg>RSA-SHA256</me:alg>
                    <me:sig>{signature}</me:sig>
                </me:env>
            </diaspora>
        """


DIASPORA_POST_SIMPLE = """<XML>
      <post>
        <status_message>
          <raw_message>((status message))</raw_message>
          <guid>((guid))</guid>
          <diaspora_handle>alice@alice.diaspora.example.org</diaspora_handle>
          <public>false</public>
          <created_at>2011-07-20 01:36:07 UTC</created_at>
        </status_message>
      </post>
    </XML>
"""

DIASPORA_POST_COMMENT = """<XML>
      <post>
        <comment>
          <guid>((guid))</guid>
          <parent_guid>((parent_guid))</parent_guid>
          <author_signature>((base64-encoded data))</author_signature>
          <text>((text))</text>
          <diaspora_handle>alice@alice.diaspora.example.org</diaspora_handle>
        </comment>
      </post>
    </XML>
"""

DIASPORA_POST_LIKE = """<XML>
      <post>
        <like>
          <target_type>Post</target_type>
          <guid>((guid))</guid>
          <parent_guid>((parent_guid))</parent_guid>
          <author_signature>((base64-encoded data))</author_signature>
          <positive>true</positive>
          <diaspora_handle>alice@alice.diaspora.example.org</diaspora_handle>
        </like>
      </post>
    </XML>
"""

DIASPORA_REQUEST = """<XML>
      <post>
        <request>
          <sender_handle>bob@example.com</sender_handle>
          <recipient_handle>alice@alice.diaspora.example.org</recipient_handle>
        </request>
      </post>
    </XML>
"""

DIASPORA_PROFILE = """<XML>
    <post>
        <profile>
            <diaspora_handle>bob@example.com</diaspora_handle>
            <first_name>Bob Bobertson</first_name>
            <last_name></last_name>
            <image_url>https://example.com/uploads/images/thumb_large_c833747578b5.jpg</image_url>
            <image_url_small>https://example.com/uploads/images/thumb_small_c8b147578b5.jpg</image_url_small>
            <image_url_medium>https://example.com/uploads/images/thumb_medium_c8b1aab04f3.jpg</image_url_medium>
            <gender></gender>
            <bio>A cool bio</bio>
            <location>Helsinki</location>
            <searchable>true</searchable>
            <nsfw>false</nsfw>
            <tag_string>#socialfederation #federation</tag_string>
        </profile>
    </post>
</XML>
"""
