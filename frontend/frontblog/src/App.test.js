import { render, screen } from '@testing-library/react';
import Blog from './Components/Blog';

test('renders learn react link', () => {
  render(<Blog />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
