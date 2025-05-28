import React from 'react';
import { format } from 'timeago.js';
import { LikeFilled, LikeOutlined, CommentOutlined } from '@ant-design/icons';
import { Card, Dropdown } from 'react-bootstrap';
import { randomAvatar } from '../../utils/randomAvatar';
import axiosService from '../../helper/axios';

function Post(props) {
    const { post, refresh } = props;
    console.log(post);

    const handleLikeClick = (action) => {
        axiosService
            .post(`/post/${post.id}/${action}`)
            .then(() => {
                refresh();
            })
            .catch((err) => console.error(err));
    };

    return (
        <>
            <Card className="rounded-3 my-4">
                <Card.Body>
                    {/* Post Header */}
                    <div className="d-flex align-items-center mb-2">
                        <img
                            src={randomAvatar(post.author.id)}
                            alt="author Avatar"
                            className="rounded-circle me-2"
                            width={40}
                            height={40}
                        />
                        <div>
                            <strong>{post.author.authorname}</strong>
                            <div
                                className="text-muted"
                                style={{ fontSize: '0.8em' }}
                            >
                                {format(post.created_at)}
                            </div>
                        </div>
                        <div className="ms-auto">
                            <Dropdown>
                                <Dropdown.Toggle variant="link" className="p-0">
                                    ...
                                </Dropdown.Toggle>
                                <Dropdown.Menu>
                                    <Dropdown.Item>Edit</Dropdown.Item>
                                    <Dropdown.Item>Delete</Dropdown.Item>
                                </Dropdown.Menu>
                            </Dropdown>
                        </div>
                    </div>

                    {/* Post Content */}
                    <div className="mb-2">{post.body}</div>

                    {/* Optional Image */}
                    {post.image && (
                        <img
                            src={post.image}
                            alt="Post"
                            className="img-fluid rounded"
                        />
                    )}

                    {/* Actions */}
                    <div className="d-flex align-items-center mt-2">
                        {post.liked ? (
                            <LikeFilled
                                onClick={() => handleLikeClick('unlike')}
                                style={{
                                    color: 'red',
                                    cursor: 'pointer',
                                    fontSize: '1.2em',
                                }}
                            />
                        ) : (
                            <LikeOutlined
                                onClick={() => handleLikeClick('like')}
                                style={{ cursor: 'pointer', fontSize: '1.2em' }}
                            />
                        )}
                        <span className="ms-2">{post.likes_count}</span>
                        <CommentOutlined
                            className="ms-3"
                            style={{ cursor: 'pointer', fontSize: '1.2em' }}
                        />
                    </div>
                </Card.Body>
            </Card>
        </>
    );
}

export default Post;
