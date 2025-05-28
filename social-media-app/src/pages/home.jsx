import React from 'react';
import Layout from '../components/layout';
import { Row, Col, Image } from 'react-bootstrap';
import { randomAvatar } from '../utils/randomAvatar';
import useUserActions from '../hooks/user.actions';
import CreatePost from '../components/post/CreatePost';
import useSWR from 'swr';
import Post from '../components/post/post';
import { fetcher } from '../helper/axios';

function Home() {
    const user = useUserActions().getUser;
    const posts = useSWR('/api/post', fetcher, {
        refreshInterval: 10000,
    });
    if (!user) {
        return <div>Loading!</div>;
    }

    return (
        <Layout>
            <Row className="justify-content-evenly">
                <Col sm={7}>
                    <Row className="border rounded align-items-center">
                        <Col className="flex-shrink-1">
                            <Image
                                src={randomAvatar()}
                                roundedCircle
                                width={52}
                                height={52}
                                className="my-2"
                            />
                        </Col>
                        <Col sm={10} className="flex-grow-1">
                            <CreatePost />
                        </Col>
                    </Row>
                    <Row className="my-4">
                        {posts?.data?.results &&
                        posts.data.results.length > 0 ? (
                            posts.data.results.map((post, index) => (
                                <Post
                                    key={post.id}
                                    post={post}
                                    refresh={posts.mutate}
                                />
                            ))
                        ) : (
                            <div className="text-center w-100">
                                No posts yet.
                            </div>
                        )}
                    </Row>
                </Col>
            </Row>
        </Layout>
    );
}

export default Home;
