export const randomAvatar = () => {
  const randomId = Math.floor(Math.random() * 60) + 1;
  return `https://i.pravatar.cc/300?img=${randomId}`;
};
