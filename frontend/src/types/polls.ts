export interface Option {
  id: number;
  text: string;
  votes: number;
}

export interface Poll {
  id: number;
  title: string;
  description: string;
  is_active: boolean;
  created_at: string;
  options: Option[];
  owner: string;
}
